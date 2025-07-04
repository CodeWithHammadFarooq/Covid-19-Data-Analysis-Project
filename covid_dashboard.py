
import plotly.express as px
import plotly.graph_objs as go

# Load data
covid_df = pd.read_csv("covid_19_india.csv")
vaccine_df = pd.read_csv("covid_vaccine_statewise.csv")

# Preprocessing
covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace=True, axis=1)
covid_df['Date'] = pd.to_datetime(covid_df['Date'], format='%Y-%m-%d')
covid_df['Active_Cases'] = covid_df['Confirmed'] - (covid_df['Cured'] + covid_df['Deaths'])

statewise = pd.pivot_table(covid_df, values=["Confirmed", "Deaths", "Cured"], index="State/UnionTerritory", aggfunc=max)
statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]
statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]
statewise = statewise.sort_values(by="Confirmed", ascending=False)

top_10_active_cases = covid_df.groupby(by='State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by='Active_Cases', ascending=False).reset_index()
top_10_deaths = covid_df.groupby(by="State/UnionTerritory").max()[['Deaths', 'Date']].sort_values(by=['Deaths'], ascending=False).reset_index()

vaccine_df.rename(columns={'Updated On': 'Vaccine_Date'}, inplace=True)
vaccine_df['Vaccine_Date'] = pd.to_datetime(vaccine_df['Vaccine_Date'], errors='coerce', dayfirst=True)
vaccine = vaccine_df[vaccine_df.State != 'India']
vaccine.rename(columns={"Total Individuals Vaccinated": "Total"}, inplace=True)

max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values('Total', ascending=False)[:5]

vaccine_progress = vaccine_df.groupby('Vaccine_Date')['Total Doses Administered'].sum().cumsum()
top_vac_states = vaccine.groupby('State')['Total Doses Administered'].sum().sort_values(ascending=False).head(10)

male = vaccine_df["Male(Individuals Vaccinated)"].sum()
female = vaccine_df["Female(Individuals Vaccinated)"].sum()
labels = ['Male', 'Female']
sizes = [male, female]

# Initialize Dash app
app = dash.Dash(__name__)

# 1. Trend of Total Confirmed, Cured, and Deaths Cases Over Time
trend_fig = px.line(
    covid_df.groupby('Date')[['Confirmed', 'Cured', 'Deaths']].sum().reset_index(),
    x='Date', y=['Confirmed', 'Cured', 'Deaths'],
    labels={'value': 'Number of Cases', 'variable': 'Case Type'},
    title='COVID-19 Trend in India Over Time'
)

# 2. Recovery and Mortality Rate by State
recovery_mortality_fig = px.bar(
    statewise.reset_index(),
    x='State/UnionTerritory',
    y=['Recovery Rate', 'Mortality Rate'],
    barmode='group',
    title='Recovery and Mortality Rate by State'
)
recovery_mortality_fig.update_layout(xaxis_tickangle=-45)

# 3. Vaccination Progress Over Time
vaccine_progress_fig = px.line(
    vaccine_progress.reset_index(),
    x='Vaccine_Date', y='Total Doses Administered',
    title='Cumulative COVID-19 Vaccine Doses Administered in India'
)

# 4. Top 10 States by Total Doses Administered
top_vac_states_fig = px.bar(
    top_vac_states.reset_index(),
    x='State', y='Total Doses Administered',
    title='Top 10 States by Total Vaccine Doses Administered'
)

# 5. Gender-wise Vaccination Distribution
gender_pie_fig = px.pie(
    names=labels, values=sizes,
    title='Gender-wise Vaccination Distribution',
    color=labels, color_discrete_map={'Male': '#3498db', 'Female': '#e74c3c'}
)

# 6. Top 10 States with Most Active Cases
top_10_active_fig = px.bar(
    top_10_active_cases.iloc[:10],
    x='State/UnionTerritory', y='Active_Cases',
    title='Top 10 States with Most Active Cases in India'
)

# 7. Top 10 States with Most Deaths
top_10_deaths_fig = px.bar(
    top_10_deaths.iloc[:10],
    x='State/UnionTerritory', y='Deaths',
    title='Top 10 States with Most Deaths'
)

# Layout
app.layout = html.Div([
    html.H1("COVID-19 India Dashboard", style={'textAlign': 'center'}),
    dcc.Tabs([
        dcc.Tab(label='Overview', children=[
            dcc.Graph(figure=trend_fig),
            dcc.Graph(figure=recovery_mortality_fig),
        ]),
        dcc.Tab(label='Vaccination', children=[
            dcc.Graph(figure=vaccine_progress_fig),
            dcc.Graph(figure=top_vac_states_fig),
            dcc.Graph(figure=gender_pie_fig),
        ]),
        dcc.Tab(label='Statewise Analysis', children=[
            dcc.Graph(figure=top_10_active_fig),
            dcc.Graph(figure=top_10_deaths_fig),
            html.H3("Statewise Summary Table"),
            dash_table.DataTable(
                data=statewise.reset_index().to_dict('records'),
                columns=[{"name": i, "id": i} for i in statewise.reset_index().columns],
                page_size=10,
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left'},
            ),
        ]),
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
