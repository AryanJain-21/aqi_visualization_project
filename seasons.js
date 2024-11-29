// Load the JSON data and create the chart
function createAQIChart(jsonDataPath) {
    // Set up the SVG canvas dimensions
    const width = 800, height = 500, margin = { top: 50, right: 200, bottom: 50, left: 60 };
  
    const svg = d3.select("body").append("svg")
      .attr("width", width)
      .attr("height", height);
  
    // Load the data
    d3.json(jsonDataPath).then(data => {
      // Define scales
      const xScale = d3.scalePoint()
        .domain(["Winter", "Spring", "Summer", "Fall"])
        .range([margin.left, width - margin.right]);
  
      const yScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.AQI)]).nice()
        .range([height - margin.bottom, margin.top]);
  
      const colorScale = d3.scaleOrdinal(d3.schemeCategory10)
        .domain([...new Set(data.map(d => d.Region))]);
  
      // Axes
      svg.append("g")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(xScale))
        .selectAll("text")
        .style("text-anchor", "middle");
  
      svg.append("g")
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(yScale))
        .append("text")
        .attr("fill", "black")
        .attr("x", -margin.left + 10)
        .attr("y", margin.top - 10)
        .attr("class", "axis-label")
        .text("Average AQI");
  
      // Nest data by region and year
      const nestedData = d3.groups(data, d => d.Region, d => d.Year);
  
      // Line generator
      const line = d3.line()
        .x(d => xScale(d.Season))
        .y(d => yScale(d.AQI));
  
      // Plot each region's line for each year
      nestedData.forEach(([region, years]) => {
        years.forEach(([year, values]) => {
          svg.append("path")
            .datum(values)
            .attr("class", "line")
            .attr("d", line)
            .attr("stroke", colorScale(region))
            .attr("stroke-width", 2)
            .attr("stroke-dasharray", year === 1980 ? "5,5" : "0"); // Different dash styles for years
        });
      });
  
      // Add a legend
      const legend = svg.append("g")
        .attr("transform", `translate(${width - margin.right + 20},${margin.top})`);
  
      // Add region-based legend
      nestedData.forEach(([region], i) => {
        legend.append("rect")
          .attr("x", 0)
          .attr("y", i * 40)
          .attr("width", 10)
          .attr("height", 10)
          .attr("fill", colorScale(region));
  
        legend.append("text")
          .attr("x", 20)
          .attr("y", i * 40 + 9)
          .attr("class", "legend")
          .text(region);
      });
  
      // Add year-based legend
      const yearLegend = legend.append("g")
        .attr("transform", `translate(0,${nestedData.length * 40})`);
  
      yearLegend.append("line")
        .attr("x1", 0)
        .attr("x2", 20)
        .attr("y1", 10)
        .attr("y2", 10)
        .attr("stroke", "black")
        .attr("stroke-width", 2)
        .attr("stroke-dasharray", "5,5");
  
      yearLegend.append("text")
        .attr("x", 30)
        .attr("y", 15)
        .text("1980");
  
      yearLegend.append("line")
        .attr("x1", 0)
        .attr("x2", 20)
        .attr("y1", 30)
        .attr("y2", 30)
        .attr("stroke", "black")
        .attr("stroke-width", 2);
  
      yearLegend.append("text")
        .attr("x", 30)
        .attr("y", 35)
        .text("2024");
    });
  }
  