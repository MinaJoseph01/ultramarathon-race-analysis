# %%
import pandas as pd
import seaborn as sns

# %%
# Load the dataset
df = pd.read_csv(r'F:\data analysis\archive\TWO_CENTURIES_OF_UM_RACES.csv')

# %%
# Display the first few rows of the dataframe
df.head()

# %%
# Display summary information about the dataframe
df.info()

# %%
# Display descriptive statistics for numerical columns
df.describe()

# %%
# Display the shape of the dataframe (rows, columns)
df.shape

# %%
# Examine the distribution of 'Event distance/length'
df['Event distance/length'].value_counts()

# %%
# Filter the dataframe for events with a distance of 50Km
df[df['Event distance/length'] == '50Km']

# %%
# Filter the dataframe for events with a distance of 50mi
df[df['Event distance/length'] == '50mi']

# %%
# Filter the dataframe for events with distances of 50Km or 50mi
df[df['Event distance/length'].isin(['50Km', '50mi'])]

# %%
# Filter for events in 2020 with distances of 50Km or 50mi held in the USA
df[(df['Event distance/length'].isin(['50Km', '50mi'])) & 
   (df['Year of event'] == 2020) & 
   (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]

# %%
# Filter the dataframe for events held in the USA
df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']

# %%
# Step 1: Filter for 'Event distance/length'
df_filtered = df[df['Event distance/length'].isin(['50Km', '50mi'])]

# Step 2: Filter for 'Year of event'
df_filtered = df_filtered[df_filtered['Year of event'] == 2020]

# Step 3: Extract the country from 'Event name' and filter for 'USA'
df_filtered = df_filtered[df_filtered['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']

# Display the resulting DataFrame
print(df_filtered)

# %%
# Display the first few rows of the filtered dataframe
df_filtered.head()

# %%
# Display the shape of the filtered dataframe (rows, columns)
df_filtered.shape

# %%
# Remove the country information from 'Event name'
df_filtered['Event name'] = df_filtered['Event name'].str.split('(').str.get(0)

# %%
# Display the filtered dataframe
df_filtered

# %%
# Calculate athlete age based on the year of birth and the event year (2020)
df_filtered['Athlete_age'] = 2020 - df_filtered['Athlete year of birth']

# %%
# Extract the numeric part of 'Athlete performance' (hours)
df_filtered['Athlete performance'] = df_filtered['Athlete performance'].str.split('h').str.get(0)

# %%
# Display the dataframe after transformations
df_filtered

# %%
# Drop unnecessary columns
df_filtered = df_filtered.drop(['Athlete country', 'Athlete club', 'Athlete year of birth', 'Athlete age category'], axis=1)

# %%
# Display the dataframe after dropping columns
df_filtered

# %%
# Check for missing values
df_filtered.isna().sum()

# %%
# Display rows with missing values in 'Athlete_age'
df_filtered[df_filtered['Athlete_age'].isna() == 1]

# %%
# Drop rows with missing values
df_filtered = df_filtered.dropna()

# %%
# Display the shape of the dataframe after dropping missing values
df_filtered.shape

# %%
# Check for duplicate rows
df_filtered[df_filtered.duplicated() == True]

# %%
# Reset the index of the dataframe
df_filtered.reset_index(drop=True, inplace=True)

# %%
# Display the data types of the dataframe columns
df_filtered.dtypes

# %%
# Convert 'Athlete_age' to integer
df_filtered['Athlete_age'] = df_filtered['Athlete_age'].astype(int)

# %%
# Convert 'Athlete average speed' to float
df_filtered['Athlete average speed'] = df_filtered['Athlete average speed'].astype(float)

# %%
# Display the data types after conversion
df_filtered.dtypes

# %%
# Display the first few rows of the final dataframe
df_filtered.head()
