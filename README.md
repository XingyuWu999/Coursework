# Project Description
The aim of this project is to analyse data on population change in London from 2012 to 2023, including population trends, migration, births and deaths. The project provides insights into London's changing population through data cleaning, database storage and visualisation and analysis. The project includes code, a database, and an analysis report that describes in detail the process of processing and analysing the data.

# Installation and Operation Guide
1. Environmental settings
Create a virtual environment and activate
Installing dependencies：
pip install -r requirements.txt

2. Data preparation
Please place the Excel data file theanalysisofpopulationestimatestool2023ew.xlsx in the project root directory. The code will automatically load the file and perform data cleaning.

3. Database creation and data storage
Run the following script to create a SQLite database and store the data:
python pratice.py

This script will read the data from the Excel file, clean and process the information, and then store it in the population_data.db database.

4. Data Analysis and Visualisation
When the pratice.py script is run, three visualisations are automatically generated:
London population trend graph (2012-2023)
Migration trend charts (net internal versus net international migration)
Chart of the number of births and deaths
These charts will help to better understand trends and changes in the population data.