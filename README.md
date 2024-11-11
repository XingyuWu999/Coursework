## Project Description

The aim of this project is to analyze data on population change in London from 2012 to 2023, including population trends, migration, births, and deaths. The project provides insights into London's changing population through data cleaning, database storage, visualization, and analysis. The project includes code, a database, and an analysis report that describes in detail the process of processing and analyzing the data.

## Installation and Operation Guide

### 1. Environmental Settings

1. Create and activate the virtual environment

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### 2. Data Preparation

Place the Excel data file `theanalysisofpopulationestimatestool2023ew.xlsx` in the project root directory. The code will automatically load the file and perform data cleaning.

Be sure to open the Excel file before running the code and select the Geography option as LONDON in any worksheet with data and save it. This ensures that the code reads London data correctly and not the rest of the UK.

### 3. Database Creation and Data Storage

Run the following script to create an SQLite database and store the data:

```sh
python pratice.py
```

This script will read the data from the Excel file, clean and process the information, and then store it in the `population_data.db` database.

### 4. Data Analysis and Visualization

When the `pratice.py` script is run, three visualizations are automatically generated:

- London population trend graph (2012-2023)
- Migration trend charts (net internal versus net international migration)
- Chart of the number of births and deaths

These charts will help to better understand trends and changes in the population data.