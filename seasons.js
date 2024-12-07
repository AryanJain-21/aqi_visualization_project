function createAQICharts(jsonDataPath) {
  const width = 300,
    height = 200,
    margin = { top: 40, right: 50, bottom: 40, left: 50 };

  d3.json(jsonDataPath).then((data) => {
    const groupedData = d3.group(data, (d) => d.Region);

    const container = d3
      .select("#aqi-trends-container")
      .style("display", "grid")
      .style("grid-template-columns", "1fr 1fr")
      .style("gap", "20px");

    groupedData.forEach((regionData, region) => {
      const chartContainer = container
        .append("div")
        .classed("chart-container", true)
        .style("text-align", "center");

      chartContainer
        .append("h4")
        .text(`AQI Seasonal Trends: ${region}`);

      const svg = chartContainer
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      const xScale = d3
        .scalePoint()
        .domain(["Winter", "Spring", "Summer", "Fall"])
        .range([0, width]);

      const yScale = d3
        .scaleLinear()
        .domain([0, d3.max(regionData, (d) => d.AQI)])
        .nice()
        .range([height, 0]);

      svg
        .append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(xScale).ticks(4));

      svg.append("g").call(d3.axisLeft(yScale).ticks(5));

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

      const line = d3
        .line()
        .x((d) => xScale(d.Season))
        .y((d) => yScale(d.AQI));

      const yearGroupedData = d3.group(regionData, (d) => d.Year);

      yearGroupedData.forEach((yearData, year) => {
        svg
          .append("path")
          .datum(yearData)
          .attr("fill", "none")
          .attr("stroke", year === 1980 ? "blue" : "red")
          .attr("stroke-dasharray", year === 1980 ? "4,4" : null)
          .attr("stroke-width", 1.5)
          .attr("d", line);
      });

      const legend = svg
        .append("g")
        .attr("transform", `translate(${width - margin.right},${margin.top - 60})`);

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
