### DS4200 Final Project: Aryan Jain, Alex Sun, Kiara Brcic Sutton, and Sara Shee

Data Downloads: https://drive.google.com/drive/folders/1I_8PbrFG7xKdVbasirJzsVd-QwY0ZBHq?usp=sharing

All data is from the [EPA](https://aqs.epa.gov/aqsweb/airdata/download_files.html#AQI) and the [Census Bureau](https://www.census.gov/data/tables/time-series/dec/density-data-text.html). Sources are listed at the bottom of the website.

# AQI Visualization Report

[Website Link](https://aryanjain-21.github.io/aqi_visualization_project/)

### 1980 and 2024 Choropleth Displaying Average AQI of States

**Marks and Channels**:  
This choropleth involves the use of polygons for states and color for encoding average AQI values. Light to dark red gradient represents increasing AQI. The tooltip interaction shows the exact AQI value and state name on hover.

**Rationale**:  
The choropleth map does a good job in showing geographic patterns in air quality and thus makes it easy to compare AQI levels among states, as well as the change over time (from 1980 to 2024). Color gradients intuitively show the severity of AQI, while a supporting legend allows for quick interpretation of the color scale.

---

### Category of AQI Distribution

**Marks and Channels**:  
The bars in the stacked bar charts represent the frequency of each AQI category within a region. The height of each bar shows the total count, while the sections within the bars represent the different AQI categories. The color of each section in the bar chart indicates the AQI category, with darker blue showing "Very Unhealthy" and lighter blue showing "Good." The position along the x-axis groups the data by region, and the y-axis shows the total frequency.

**Rationale**:  
This design makes it easy to see how air quality varies across regions and over time. The stacked bars clearly show how much each category contributes to the overall AQI distribution for a region. Using shades of blue helps visually emphasize the most polluted categories while keeping the chart clean and easy to read.

---

### Significant Events and AQI

**Marks and Channels**:  
This line chart uses points and lines as marks to represent the annual average AQI values over time. The x-axis encodes the year, while the y-axis encodes the average AQI. Annotations are included as text labels and dashed vertical lines to highlight key environmental events (e.g., Clean Air Act Amendments, Montreal Protocol). Red circular markers are used to emphasize specific events on the trend line, enhancing visibility.

**Rationale**:  
The line chart effectively illustrates the temporal progression of AQI trends, making it easy to observe significant drops or spikes in response to major environmental events or external factors. The annotations provide critical context, linking policy changes, natural disasters, and economic shifts to variations in AQI. The combination of position (for quantitative data), text annotations, and markers ensures clarity and allows viewers to derive insights about the impact of events like the Clean Air Act or Canadian wildfires on air quality over time.

---

### AQI Trends for Top/Bottom States

**Marks and Channels**:  
The lines in the line graphs represent AQI trends over time for each state. Each line corresponds to one state, and the data points show the actual values for 1980 and 2021. The position of the lines on the x-axis shows the year (1980 and 2021), while the y-axis indicates the average AQI value. The color of the lines differentiates the states, making it easy to track individual trends.

**Rationale**:  
This design highlights changes in AQI over time for the most and least polluted states. The lines make it easy to compare trends between states, while the markers on the lines emphasize the specific data points for the two years. This approach visually tells the story of improvement or worsening air quality in a straightforward way.

---

### Histogram of Average AQI of States

**Marks and Channels**:  
This visualization presents the average Air Quality Index (AQI) for each U.S. state (x-axis) across a user-selected year, ranging from 2000 to 2024. The AQI values are displayed on the y-axis as vertical bars, with a gradient color scale from light blue to dark blue indicating increasing AQI levels. Interactive tooltips provide additional details, such as the state name, AQI value, and selected year, when hovering over a bar.

**Rationale**:  
Bar charts are ideal for comparing AQI values across multiple states. The interactive year selector enables dynamic analysis of AQI trends over time. The color gradient enhances the ability to quickly identify states with relatively higher or lower AQI values, making the visualization both intuitive and informative.

---

### Seasonal AQI Trends

**Marks and Channels**:  
The visualization illustrates AQI trends across the seasons (x-axis) for each region and year by using lines; it maps AQI values against the y-axis. Colors differentiate between years, such as using blue for 1980 and red for 2023, while dashed lines bring clarity to the trends in the year 1980.

**Rationale**:  
Line charts are a good visualization method to represent seasonality and trending. Color and dashes allow year-over-year comparisons to be intuitive.

---

### Population Density and AQI

**Marks and Channels**:  
This scatter plot uses points as marks to represent individual states, with position along the x-axis encoding Resident Population Density and the y-axis encoding Air Quality Index (AQI). Color is used as a channel to differentiate regions (i.e., New England, Midwest), and size of the points remains constant. Interactive elements include a year slider to filter data by year and radio buttons for regional filtering. Hovering over each point also shows the state name.

**Rationale**:  
The scatter plot effectively visualizes the relationship between population density and AQI for each state, making it easy to observe regional patterns and trends over time. The use of position ensures quantitative comparisons, while color coding allows users to distinguish regional differences intuitively. The year slider enhances temporal analysis, and region-based filtering helps isolate specific areas for deeper investigation. This combination of interactivity and intuitive design supports a thorough exploration of how population density correlates with air quality across time and regions.

