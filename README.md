"# Covid-19-Data-Analysis-Project" 
Project Description: Vaccination Data Analysis and Processing
This project focuses on analyzing and processing vaccination data to gain insights into the vaccination drive, including gender-based vaccination trends, age group statistics, and overall vaccine administration. Below is a detailed description of the various steps and challenges addressed during the project:

Objective:
The primary goal of this project is to process and analyze vaccination data stored in Excel format, generate visualizations for key trends, and convert the processed data into CSV format for further usage.

Key Tasks and Processes:
Data Import and Exploration:

The project begins by loading the vaccination dataset from an Excel file using the Pandas library.
Initial exploration includes identifying columns, understanding data types, and handling null values in the dataset.
Data Cleaning:

Redundant columns such as 'AEFI' and certain age-specific dose columns were dropped to focus on relevant data.
Missing data and inconsistencies in column names, such as 'SputniV (Doses Administered)' vs. 'Sputnik V (Doses Administered)', were resolved to ensure smooth analysis.
Data Transformation:

The cleaned dataset was transformed to make it suitable for analysis. This included:
Summing up gender-specific and age-specific vaccination numbers.
Renaming columns to consistent and understandable formats.
Conversion of processed data into CSV format for sharing and external usage.
Data Visualization:

Created a gender-based pie chart to compare the proportion of male and female vaccinations.
Used the plotly library for creating interactive and visually appealing visualizations.
Challenges Encountered and Solutions:

File Path Issues: The project encountered FileNotFoundError multiple times due to incorrect file paths. These were resolved by verifying the file locations and correcting path references.
Column Name Discrepancies: The dataset had mismatched or unexpected column names, which were corrected through inspection and renaming.
Data Type Handling: Null values in numeric columns were replaced with appropriate defaults to allow smooth calculations.
File Conversion:

After analysis, the cleaned data was saved in CSV format using Pandas. This step ensured compatibility with other tools and future analyses.
Technologies Used:
Python Libraries:
Pandas: For data manipulation and cleaning.
Plotly: For data visualization.
OS: For file system interactions.
Data Formats: Excel (.xlsx) and CSV (.csv).
Outcome:
A cleaned and well-structured dataset ready for further analysis.
Visualizations showcasing vaccination trends based on gender.
Exported CSV file for seamless sharing and integration with other tools.
Future Scope:
Extend the analysis to include geographical trends and time-series analysis.
Incorporate machine learning techniques to predict vaccination rates.
Automate the data cleaning and processing pipeline for similar datasets.
This project provides a robust framework for handling and analyzing vaccination datasets, overcoming real-world challenges like file inconsistencies, data mismatches, and null values. It also demonstrates a strong understanding of Python for data analysis.






