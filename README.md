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
   git clone https://github.com/MinaJoseph01/ultramarathon-race-analysis.git



Key Skills
Data cleaning and preprocessing
Data filtering and extraction
Feature engineering
Handling missing values and duplicates
Data visualization with Seaborn
Tools Used
Python (Pandas, Seaborn)
Jupyter Notebook
Feel free to modify the code and add more visualizations or analyses based on the dataset. Contributions and feedback are welcome!

About the Dataset
According to Wikipedia, an ultramarathon, also called ultra distance or ultra running, is any footrace longer than the traditional marathon length of 42.195 kilometers (26 mi 385 yd). Various distances are raced competitively, from the shortest common ultramarathon of 31 miles (50 km) to over 200 miles (320 km). 50k and 100k are both World Athletics record distances, but some 100 miles (160 km) races are among the oldest and most prestigious events, especially in North America.

The data in this file is a large collection of ultramarathon race records registered between 1798 and 2022 (a period of well over two centuries) being therefore a formidable long term sample. All data was obtained from public websites.

Despite the original data being of public domain, the race records, which originally contained the athletes' names, have been anonymized to comply with data protection laws and to preserve the athletes' privacy. However, a column Athlete ID has been created with a numerical ID representing each unique runner (so if Antonio Fernández participated in 5 races over different years, then the corresponding race records now hold his unique Athlete ID instead of his name). This way valuable information has been preserved.

The dataset contains 7,461,226 ultramarathon race records from 1,641,168 unique athletes. The following columns (with data types) are included:

Year of event (int64)
Event dates (object)
Event name (object)
Event distance/length (object)
Event number of finishers (int64)
Athlete performance (object)
Athlete club (object)
Athlete country (object)
Athlete year of birth (float64)
Athlete gender (object)
Athlete age category (object)
Athlete average speed (object)
Athlete ID (int64)
The Event name column includes country location information that can be derived to a new column, and similarly seasonal information can be found in the Event dates column beyond the Year of event (these can be extracted with a bit of processing).

The Event distance/length column describes the type of race, covering the most popular UM race distances and lengths, and some
   
