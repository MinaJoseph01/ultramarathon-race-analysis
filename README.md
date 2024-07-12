# Ultramarathon Race Analysis

This repository contains the code and analysis performed on a dataset of ultramarathon race records from 1798 to 2022. The analysis aimed to explore the performance of athletes in 50Km and 50mi races in the USA during the year 2020. The project includes detailed steps for data cleaning, preprocessing, and analysis.

## Project Overview

The ultramarathon dataset is a comprehensive collection of race records, including key information such as event name, distance, athlete performance, and more. The analysis involved several steps:

1. **Data Loading and Initial Exploration:**
   - The dataset is loaded from a CSV file, and initial exploration is done using `head()`, `info()`, `describe()`, and `shape()` methods.

2. **Data Filtering:**
   - The dataset is filtered to include only events with distances of 50Km and 50mi.
   - Further filtering is done to include only events held in the year 2020 and in the USA.

3. **Data Transformation:**
   - The 'Event name' column is cleaned to remove country information.
   - Athlete age is calculated based on the year of birth and the event year.
   - The numeric part of 'Athlete performance' is extracted.

4. **Data Cleaning:**
   - Unnecessary columns are dropped to simplify the dataset.
   - Missing values are handled by dropping rows with `NaN` values.
   - Duplicate rows are checked and the index is reset.

5. **Data Type Conversion:**
   - Columns are converted to appropriate data types (`int` for 'Athlete_age' and `float` for 'Athlete average speed').

## Files

- `ultramarathon_analysis.ipynb`: Jupyter notebook containing the complete analysis code and visualizations.
- `TWO_CENTURIES_OF_UM_RACES.csv`: Original dataset used for the analysis.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ultramarathon-race-analysis.git
