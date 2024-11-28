import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
aqi_1980 = pd.read_csv('../daily_aqi_by_county_1980.csv')
aqi_2021 = pd.read_csv('../daily_aqi_by_county_2021.csv')

# Convert Date columns to datetime format and extract year
aqi_1980['Date'] = pd.to_datetime(aqi_1980['Date'], errors='coerce')
aqi_1980['Year'] = aqi_1980['Date'].dt.year

aqi_2021['Date'] = pd.to_datetime(aqi_2021['Date'], errors='coerce')
aqi_2021['Year'] = aqi_2021['Date'].dt.year

# Combine the two datasets
combined_aqi = pd.concat([aqi_1980, aqi_2021], ignore_index=True)

# 1. Multi-Line Chart: Average AQI Trends for Top and Bottom 5 States
# Calculate the average AQI for each state by year
state_avg_aqi = combined_aqi.groupby(['Year', 'State Name'])['AQI'].mean().reset_index()

# Identify the top 5 most polluted and bottom 5 least polluted states based on 1980 data
state_avg_1980 = state_avg_aqi[state_avg_aqi['Year'] == 1980].sort_values(by='AQI', ascending=False)
top_5_states = state_avg_1980.head(5)['State Name']
bottom_5_states = state_avg_1980.tail(5)['State Name']

# Filter the data for these states across both years
filtered_states = state_avg_aqi[state_avg_aqi['State Name'].isin(pd.concat([top_5_states, bottom_5_states]))]

# Multi-Line Chart
plt.figure(figsize=(8, 6))
# Plot top 5 states with solid lines
for state in top_5_states:
    state_data = filtered_states[filtered_states['State Name'] == state]
    plt.plot(state_data['Year'], state_data['AQI'], marker='o', label=f'Top: {state}')

# Plot bottom 5 states with dashed lines
for state in bottom_5_states:
    state_data = filtered_states[filtered_states['State Name'] == state]
    plt.plot(state_data['Year'], state_data['AQI'], linestyle='--', marker='x', label=f'Bottom: {state}')

plt.title('AQI Trends for Top and Bottom 5 States (1980 vs 2021)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average AQI', fontsize=14)
plt.xticks([1980, 2021], fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("multi_line_aqi_trends.png")
plt.show()

# 2. Stacked Bar Chart: AQI Category Distribution by Region
# Define regions
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

# Assign regions to both datasets
combined_aqi['Region'] = 'Other' # Default value
for region, states in regions.items():
    combined_aqi.loc[combined_aqi['State Name'].isin(states), 'Region'] = region

# Group by region and category for 1980 and 2021 separately
region_category_1980 = combined_aqi[combined_aqi['Year'] == 1980].groupby(['Region', 'Category']).size().unstack(fill_value=0)
region_category_2021 = combined_aqi[combined_aqi['Year'] == 2021].groupby(['Region', 'Category']).size().unstack(fill_value=0)

# Plot stacked bar charts
fig, ax = plt.subplots(1, 2, figsize=(6, 4), sharey=True)
region_category_1980.plot(kind='bar', stacked=True, colormap='viridis', edgecolor='black', ax=ax[0])
ax[0].set_title('AQI Category Distribution by Region (1980)', fontsize=14)
ax[0].set_xlabel('Region', fontsize=12)
ax[0].set_ylabel('Frequency', fontsize=12)
ax[0].tick_params(axis='x', rotation=45)

region_category_2021.plot(kind='bar', stacked=True, colormap='viridis', edgecolor='black', ax=ax[1])
ax[1].set_title('AQI Category Distribution by Region (2021)', fontsize=14)
ax[1].set_xlabel('Region', fontsize=12)
ax[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
fig.savefig("stacked_bar_aqi_distribution.png")
plt.show()

# 3. Bubble Chart: Relationship Between Number of Sites Reporting and AQI by State
# Filter for 1980 and 2021 separately
bubble_1980 = combined_aqi[combined_aqi['Year'] == 1980].groupby('State Name').agg({
    'Number of Sites Reporting': 'mean',
    'AQI': 'mean',
    'State Name': 'count'
}).rename(columns={'State Name': 'Data Points'})

bubble_2021 = combined_aqi[combined_aqi['Year'] == 2021].groupby('State Name').agg({
    'Number of Sites Reporting': 'mean',
    'AQI': 'mean',
    'State Name': 'count'
}).rename(columns={'State Name': 'Data Points'})

# Plot the bubble chart for 1980
plt.figure(figsize=(6, 4))
plt.scatter(
    bubble_1980['Number of Sites Reporting'],
    bubble_1980['AQI'],
    s=bubble_1980['Data Points'] * 10,
    alpha=0.6,
    edgecolors='black',
    label='1980'
)
plt.title('Relationship Between Monitoring Sites and AQI by State (1980)', fontsize=16)
plt.xlabel('Average Number of Sites Reporting', fontsize=14)
plt.ylabel('Average AQI', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig("bubble_chart_aqi_1980.png")
plt.show()

# Plot the bubble chart for 2021
plt.figure(figsize=(6, 4))
plt.scatter(
    bubble_2021['Number of Sites Reporting'],
    bubble_2021['AQI'],
    s=bubble_2021['Data Points'] * 10,
    alpha=0.6,
    edgecolors='black',
    label='2021'
)
plt.title('Relationship Between Monitoring Sites and AQI by State (2021)', fontsize=16)
plt.xlabel('Average Number of Sites Reporting', fontsize=14)
plt.ylabel('Average AQI', fontsize=14)
plt.grid(alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.savefig("bubble_chart_aqi_2021.png")
plt.show()