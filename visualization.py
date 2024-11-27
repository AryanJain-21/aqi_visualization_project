# Reloading the dataset and redefining all variables for clarity
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
aqi_data = pd.read_csv('../daily_aqi_by_county_1980.csv')

# Convert Date column to datetime and extract year
aqi_data['Date'] = pd.to_datetime(aqi_data['Date'])
aqi_data['Year'] = aqi_data['Date'].dt.year

# Subset data for 5-year intervals (1980, 1985, ..., 2020)
years_of_interest = list(range(1980, 2025, 5))
subset_aqi = aqi_data[aqi_data['Year'].isin(years_of_interest)]

# 1. Multi-Line Chart: Average AQI Trends for the Top and Bottom 5 States in 1980
state_avg_1980 = subset_aqi[subset_aqi['Year'] == 1980].groupby('State Name')['AQI'].mean()
top_5_states_1980 = state_avg_1980.sort_values(ascending=False).head(5).index
bottom_5_states_1980 = state_avg_1980.sort_values().head(5).index

plt.figure(figsize=(14, 8))
for state in top_5_states_1980:
    state_data = subset_aqi[subset_aqi['State Name'] == state]
    plt.plot(state_data['Year'], state_data['AQI'], marker='o', label=f'Top: {state}')
for state in bottom_5_states_1980:
    state_data = subset_aqi[subset_aqi['State Name'] == state]
    plt.plot(state_data['Year'], state_data['AQI'], linestyle='--', marker='x', label=f'Bottom: {state}')

plt.title('AQI Trends for Top and Bottom 5 States in 1980')
plt.xlabel('Year')
plt.ylabel('Average AQI')
plt.xticks(years_of_interest, rotation=45)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2. Stacked Bar Chart: AQI Category Distribution by Region in 2020
# Manually assign regions
subset_aqi['Region'] = 'Other'
northeast_states = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont',
                    'New Jersey', 'New York', 'Pennsylvania']
midwest_states = ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska',
                  'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin']
south_states = ['Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland',
                'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia',
                'West Virginia']
west_states = ['Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico',
               'Oregon', 'Utah', 'Washington', 'Wyoming']

for i in subset_aqi.index:
    state = subset_aqi.at[i, 'State Name']
    if state in northeast_states:
        subset_aqi.at[i, 'Region'] = 'Northeast'
    elif state in midwest_states:
        subset_aqi.at[i, 'Region'] = 'Midwest'
    elif state in south_states:
        subset_aqi.at[i, 'Region'] = 'South'
    elif state in west_states:
        subset_aqi.at[i, 'Region'] = 'West'

# Group by region and category
region_category_distribution = subset_aqi[subset_aqi['Year'] == 2020].groupby(['Region', 'Category']).size().unstack(fill_value=0)

region_category_distribution.plot(kind='bar', stacked=True, figsize=(14, 8), colormap='viridis', edgecolor='black')
plt.title('AQI Category Distribution by Region (2020)')
plt.xlabel('Region')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.legend(title='AQI Category')
plt.tight_layout()
plt.show()

# 3. Bubble Chart: Relationship Between Number of Sites Reporting and AQI by State
subset_aqi['Number of Sites Reporting'] = pd.to_numeric(subset_aqi['Number of Sites Reporting'], errors='coerce')
bubble_data = subset_aqi.groupby('State Name').agg({
    'Number of Sites Reporting': 'mean',
    'AQI': 'mean',
    'State Name': 'count'
}).rename(columns={'State Name': 'Data Points'})

plt.figure(figsize=(14, 8))
plt.scatter(
    bubble_data['Number of Sites Reporting'],
    bubble_data['AQI'],
    s=bubble_data['Data Points'] * 10,  # Scale bubble size by number of data points
    alpha=0.6,
    edgecolors='black'
)
plt.title('Relationship Between Monitoring Sites and AQI by State')
plt.xlabel('Average Number of Sites Reporting')
plt.ylabel('Average AQI')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()