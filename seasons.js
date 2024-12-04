function createAQIChart(jsonDataPath) {
  const width = 900,
    height = 500,
    margin = { top: 50, right: 250, bottom: 50, left: 60 };
  const svg = d3
    .select("#aqi-trends-chart")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  svg
    .append("text")
    .attr("x", width / 2)
    .attr("y", margin.top / 2)
    .attr("text-anchor", "middle")
    .style("font-size", "18px")
    .style("font-weight", "bold")
    .text("AQI Trends Over Time Through Seasons");

  d3.json(jsonDataPath).then((data) => {
    const xScale = d3
      .scalePoint()
      .domain(["Winter", "Spring", "Summer", "Fall"])
      .range([margin.left, width - margin.right]);

    const yScale = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.AQI)])
      .nice()
      .range([height - margin.bottom, margin.top]);

    const colorScale = d3
      .scaleOrdinal(d3.schemeCategory10)
      .domain([...new Set(data.map((d) => d.Region))]);

    svg
      .append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .call(d3.axisBottom(xScale));

    svg
      .append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .call(d3.axisLeft(yScale));

    svg
      .append("text")
      .attr("x", width / 2)
      .attr("y", height - 30)
      .attr("text-anchor", "middle")
      .style("font-size", "14px")
      .style("font-weight", "bold")
      .text("Season");

    svg
      .append("text")
      .attr("x", -(height / 2))
      .attr("y", 20)
      .attr("text-anchor", "middle")
      .style("font-size", "14px")
      .style("font-weight", "bold")
      .attr("transform", "rotate(-90)")
      .text("AQI");

    const nestedData = d3.groups(
      data,
      (d) => d.Region,
      (d) => d.Year
    );

    const line = d3
      .line()
      .x((d) => xScale(d.Season))
      .y((d) => yScale(d.AQI));

    nestedData.forEach(([region, years]) => {
      years.forEach(([year, values]) => {
        svg
          .append("path")
          .datum(values)
          .attr("class", "line")
          .attr("d", line)
          .attr("stroke", colorScale(region))
          .attr("stroke-width", 1.5)
          .attr("stroke-dasharray", year === 1980 ? "4,4" : "0")
          .attr("fill", "none")
          .style("opacity", 0.8);
      });
    });

    const legend = svg
      .append("g")
      .attr(
        "transform",
        `translate(${width - margin.right + 20},${margin.top})`
      );

    nestedData.forEach(([region], i) => {
      legend
        .append("rect")
        .attr("x", 0)
        .attr("y", i * 20)
        .attr("width", 10)
        .attr("height", 10)
        .attr("fill", colorScale(region));

      legend
        .append("text")
        .attr("x", 20)
        .attr("y", i * 20 + 9)
        .text(region)
        .style("font-size", "12px");
    });

    const yearLegend = legend
      .append("g")
      .attr("transform", `translate(0,${nestedData.length * 20})`);

    yearLegend
      .append("line")
      .attr("x1", 0)
      .attr("x2", 20)
      .attr("y1", 10)
      .attr("y2", 10)
      .attr("stroke", "black")
      .attr("stroke-width", 1.5)
      .attr("stroke-dasharray", "4,4");

    yearLegend
      .append("text")
      .attr("x", 30)
      .attr("y", 15)
      .text("1980")
      .style("font-size", "12px");

    yearLegend
      .append("line")
      .attr("x1", 0)
      .attr("x2", 20)
      .attr("y1", 30)
      .attr("y2", 30)
      .attr("stroke", "black")
      .attr("stroke-width", 1.5);

    yearLegend
      .append("text")
      .attr("x", 30)
      .attr("y", 35)
      .text("2023")
      .style("font-size", "12px");
  });
}
