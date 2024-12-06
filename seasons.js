function createAQICharts(jsonDataPath) {
  const width = 400, // Reduced width
    height = 300, // Reduced height
    margin = { top: 40, right: 50, bottom: 40, left: 50 };

  // Fetch the data
  d3.json(jsonDataPath).then((data) => {
    // Group data by region
    const groupedData = d3.group(data, (d) => d.Region);

    // Set up the container as a 2x2 grid
    const container = d3
      .select("#aqi-trends-container")
      .style("display", "grid")
      .style("grid-template-columns", "1fr 1fr") // 2 columns
      .style("gap", "20px"); // Spacing between charts

    // Create a chart for each region
    groupedData.forEach((regionData, region) => {
      // Create a container for each chart
      const chartContainer = container
        .append("div")
        .classed("chart-container", true)
        .style("text-align", "center");

      // Add a title for the chart
      chartContainer
        .append("h4") // Smaller heading for reduced space
        .text(`AQI Trends: ${region}`);

      // Create an SVG for the chart
      const svg = chartContainer
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      // Set up scales
      const xScale = d3
        .scalePoint()
        .domain(["Winter", "Spring", "Summer", "Fall"])
        .range([0, width]);

      const yScale = d3
        .scaleLinear()
        .domain([0, d3.max(regionData, (d) => d.AQI)])
        .nice()
        .range([height, 0]);

      // Add axes
      svg
        .append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(xScale).ticks(4));

      svg.append("g").call(d3.axisLeft(yScale).ticks(5));

      // Add axes labels
      svg
        .append("text")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 5)
        .attr("text-anchor", "middle")
        .style("font-size", "10px")
        .text("Season");

      svg
        .append("text")
        .attr("x", -(height / 2))
        .attr("y", -margin.left / 2)
        .attr("text-anchor", "middle")
        .style("font-size", "10px")
        .attr("transform", "rotate(-90)")
        .text("AQI");

      // Line generator
      const line = d3
        .line()
        .x((d) => xScale(d.Season))
        .y((d) => yScale(d.AQI));

      // Group data by year within the region
      const yearGroupedData = d3.group(regionData, (d) => d.Year);

      yearGroupedData.forEach((yearData, year) => {
        // Draw the line
        svg
          .append("path")
          .datum(yearData)
          .attr("fill", "none")
          .attr("stroke", year === 1980 ? "blue" : "red")
          .attr("stroke-dasharray", year === 1980 ? "4,4" : null)
          .attr("stroke-width", 1.5)
          .attr("d", line);
      });

      // Add a legend for years
      const legend = svg
        .append("g")
        .attr("transform", `translate(${width - margin.right},${margin.top})`);

      legend
        .append("line")
        .attr("x1", 0)
        .attr("x2", 15)
        .attr("y1", 0)
        .attr("y2", 0)
        .attr("stroke", "blue")
        .attr("stroke-width", 1.5)
        .attr("stroke-dasharray", "4,4");

      legend
        .append("text")
        .attr("x", 20)
        .attr("y", 5)
        .text("1980")
        .style("font-size", "10px");

      legend
        .append("line")
        .attr("x1", 0)
        .attr("x2", 15)
        .attr("y1", 15)
        .attr("y2", 15)
        .attr("stroke", "red")
        .attr("stroke-width", 1.5);

      legend
        .append("text")
        .attr("x", 20)
        .attr("y", 20)
        .text("2023")
        .style("font-size", "10px");
    });
  });
}
