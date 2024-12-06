import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

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

# Calculate the average AQI for each state by year
state_avg_aqi = combined_aqi.groupby(['Year', 'State Name'])['AQI'].mean().reset_index()

# Identify the top 5 most polluted and bottom 5 least polluted states based on 1980 data
state_avg_1980 = state_avg_aqi[state_avg_aqi['Year'] == 1980].sort_values(by='AQI', ascending=False)
top_5_states = state_avg_1980.head(5)['State Name']
bottom_5_states = state_avg_1980.tail(5)['State Name']

# Filter the data for these states across both years
filtered_states = state_avg_aqi[state_avg_aqi['State Name'].isin(pd.concat([top_5_states, bottom_5_states]))]

# Line Chart for Top 5 Most Polluted States
plt.figure(figsize=(14, 8))
for state in top_5_states:
    state_data = filtered_states[filtered_states['State Name'] == state]
    plt.plot(state_data['Year'], state_data['AQI'], marker='o', label=state)

plt.title('AQI Trends for Top 5 Most Polluted States (1980 vs 2021)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average AQI', fontsize=14)
plt.xticks([1980, 2021], fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='State', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("most_line_aqi_trends.png")
plt.show()

# Line Chart for Bottom 5 Least Polluted States
plt.figure(figsize=(14, 8))
for state in bottom_5_states:
    state_data = filtered_states[filtered_states['State Name'] == state]
    plt.plot(state_data['Year'], state_data['AQI'], marker='o', label=state)

plt.title('AQI Trends for Bottom 5 Least Polluted States (1980 vs 2021)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average AQI', fontsize=14)
plt.xticks([1980, 2021], fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='State', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("least_line_aqi_trends.png")
plt.show()

# Stacked Bar Chart: AQI Category Distribution by Region
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
combined_aqi['Region'] = 'Other'  # Default value
for region, states in regions.items():
    combined_aqi.loc[combined_aqi['State Name'].isin(states), 'Region'] = region

# Group by region and category for 1980 and 2021 separately
region_category_1980 = combined_aqi[combined_aqi['Year'] == 1980].groupby(['Region', 'Category']).size().unstack(fill_value=0)
region_category_2021 = combined_aqi[combined_aqi['Year'] == 2021].groupby(['Region', 'Category']).size().unstack(fill_value=0)

# Custom colormap for pollution levels (light blue to dark blue)
pollution_colors = mcolors.LinearSegmentedColormap.from_list(
    "pollution_gradient", ["#7FDBFF", "#0074D9", "#001f3f"]
)

# Plot stacked bar charts
fig, ax = plt.subplots(1, 2, figsize=(16, 8), sharey=True)
region_category_1980.plot(kind='bar', stacked=True, colormap=pollution_colors, edgecolor='black', ax=ax[0])
ax[0].set_title('AQI Category Distribution by Region (1980)', fontsize=14)
ax[0].set_xlabel('Region', fontsize=12)
ax[0].set_ylabel('Frequency', fontsize=12)
ax[0].tick_params(axis='x', rotation=45)

region_category_2021.plot(kind='bar', stacked=True, colormap=pollution_colors, edgecolor='black', ax=ax[1])
ax[1].set_title('AQI Category Distribution by Region (2021)', fontsize=14)
ax[1].set_xlabel('Region', fontsize=12)
ax[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
fig.savefig("stacked_bar_aqi_distribution.png")
plt.show()