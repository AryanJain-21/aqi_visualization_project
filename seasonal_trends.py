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
regions = {
    'Northeast': ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont',
                  'New Jersey', 'New York', 'Pennsylvania'],
    'Midwest': ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska',
                'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin'],
    'South': ['Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland',
              'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia',
              'West Virginia'],
    'West': ['Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico',
             'Oregon', 'Utah', 'Washington', 'Wyoming']
}

# Map states to regions
df['Region'] = df['State Name'].map(regions)

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
