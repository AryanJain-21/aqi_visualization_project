import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('../daily_aqi_by_county_1980.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Season'] = df['Month'].map({12: 'Winter', 1: 'Winter', 2: 'Winter',
                                 3: 'Spring', 4: 'Spring', 5: 'Spring',
                                 6: 'Summer', 7: 'Summer', 8: 'Summer',
                                 9: 'Fall', 10: 'Fall', 11: 'Fall'})

# Define the state to region mapping
state_to_region = {
    'Connecticut': 'New England', 'Maine': 'New England', 'Massachusetts': 'New England', 
    'New Hampshire': 'New England', 'Rhode Island': 'New England', 'Vermont': 'New England',
    'Illinois': 'Midwest', 'Indiana': 'Midwest', 'Iowa': 'Midwest', 'Kansas': 'Midwest', 
    'Michigan': 'Midwest', 'Minnesota': 'Midwest', 'Missouri': 'Midwest', 'Nebraska': 'Midwest', 
    'North Dakota': 'Midwest', 'Ohio': 'Midwest', 'South Dakota': 'Midwest', 'Wisconsin': 'Midwest',
    'Delaware': 'South', 'Florida': 'South', 'Georgia': 'South', 'Maryland': 'South', 
    'North Carolina': 'South', 'South Carolina': 'South', 'Virginia': 'South', 'District of Columbia': 'South', 
    'West Virginia': 'South', 'Alabama': 'South', 'Kentucky': 'South', 'Mississippi': 'South', 
    'Tennessee': 'South', 'Arkansas': 'South', 'Louisiana': 'South', 'Oklahoma': 'South', 
    'Texas': 'South', 
    'Arizona': 'West', 'Colorado': 'West', 'Idaho': 'West', 'Montana': 'West', 
    'Nevada': 'West', 'New Mexico': 'West', 'Utah': 'West', 'Wyoming': 'West', 
    'Alaska': 'West', 'California': 'West', 'Hawaii': 'West', 'Oregon': 'West', 
    'Washington': 'West'
}

# Map states to regions
df['Region'] = df['State Name'].map(state_to_region)

# Group by region and season
seasonal_avg = df.groupby(['Region', 'Season'])['AQI'].mean().reset_index()

# Plotting
plt.figure(figsize=(12, 6))
for region in seasonal_avg['Region'].unique():
    region_data = seasonal_avg[seasonal_avg['Region'] == region]
    plt.plot(region_data['Season'], region_data['AQI'], label=region)

plt.title('Seasonal AQI Trends by Region')
plt.xlabel('Season')
plt.ylabel('Average AQI')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize='small')
plt.tight_layout()
plt.show()
