"""
This script analyzes London population data from 2012 to 2023, including population trends, migration, births, and deaths.
It loads the data from an Excel file, stores it in a SQLite database, and visualizes key trends.
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
FILE_PATH = r"C:\Users\15325\COMP0035 CW\Coursework\theanalysisofpopulationestimatestool2023ew.xlsx"
xls = pd.ExcelFile(FILE_PATH)

# Load the "Components of Change" sheet
components_of_change_df = pd.read_excel(xls, sheet_name='Components of Change')

# Extract relevant rows for data from 2012 to 2023
components_of_change_cleaned = components_of_change_df.iloc[4:16, 3:15].copy()

# Assign appropriate category names
category_names = [
    "Population",
    "Births",
    "Deaths",
    "Natural Change",
    "Internal In",
    "Internal Out",
    "Internal Net",
    "International In",
    "International Out",
    "International Net",
    "Special",
    "Unattributable"
]
components_of_change_cleaned.insert(0, "Category", category_names)

# Rename the columns to reflect the years from 2012 to 2023
components_of_change_cleaned.columns = ["Category"] + [f"mid_{year}" for year in range(2012, 2024)]

# Convert data to numeric values where applicable and ensure no float numbers
for col in components_of_change_cleaned.columns[1:]:
    components_of_change_cleaned[col] = pd.to_numeric(components_of_change_cleaned[col], errors='coerce').fillna(0).astype(int)

# Create SQLite database and store the data
conn = sqlite3.connect("population_data.db")
cursor = conn.cursor()

# Create a table for components of change
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS ComponentsOfChange (
        Category TEXT,
        mid_2012 INTEGER,
        mid_2013 INTEGER,
        mid_2014 INTEGER,
        mid_2015 INTEGER,
        mid_2016 INTEGER,
        mid_2017 INTEGER,
        mid_2018 INTEGER,
        mid_2019 INTEGER,
        mid_2020 INTEGER,
        mid_2021 INTEGER,
        mid_2022 INTEGER,
        mid_2023 INTEGER
    )
    '''
)

# Insert data into the table
for _, row in components_of_change_cleaned.iterrows():
    cursor.execute(
        '''
        INSERT INTO ComponentsOfChange (
            Category, mid_2012, mid_2013, mid_2014, mid_2015, mid_2016, mid_2017,
            mid_2018, mid_2019, mid_2020, mid_2021, mid_2022, mid_2023
        ) VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        ''', tuple(row)
    )

conn.commit()
conn.close()

# Population Trend Analysis
population_data = components_of_change_cleaned[components_of_change_cleaned['Category'] == 'Population'].iloc[:, 1:]
years = population_data.columns
population_values = population_data.values.flatten()

plt.figure(figsize=(10, 6))
plt.plot(years, population_values, marker='o', linestyle='-', color='b')
plt.title('Population Trend in London (2012-2023)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Migration Analysis
internal_net_data = components_of_change_cleaned[components_of_change_cleaned['Category'] == 'Internal Net'].iloc[:, 1:]
international_net_data = components_of_change_cleaned[components_of_change_cleaned['Category'] == 'International Net'].iloc[:, 1:]

internal_net_values = internal_net_data.values.flatten()
international_net_values = international_net_data.values.flatten()

plt.figure(figsize=(10, 6))
plt.plot(years, internal_net_values, marker='o', linestyle='-', color='r', label='Internal Net Migration')
plt.plot(years, international_net_values, marker='o', linestyle='-', color='g', label='International Net Migration')
plt.title('Net Migration Trend in London (2012-2023)')
plt.xlabel('Year')
plt.ylabel('Net Migration')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Births and Deaths Analysis
births_data = components_of_change_cleaned[components_of_change_cleaned['Category'] == 'Births'].iloc[:, 1:]
deaths_data = components_of_change_cleaned[components_of_change_cleaned['Category'] == 'Deaths'].iloc[:, 1:]

births_values = births_data.values.flatten()
deaths_values = deaths_data.values.flatten()

plt.figure(figsize=(10, 6))
plt.plot(years, births_values, marker='o', linestyle='-', color='c', label='Births')
plt.plot(years, deaths_values, marker='o', linestyle='-', color='m', label='Deaths')
plt.title('Births vs Deaths in London (2012-2023)')
plt.xlabel('Year')
plt.ylabel('Number of Births/Deaths')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(components_of_change_cleaned.to_string(index=False))
