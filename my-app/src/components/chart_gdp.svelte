<script>
  // imports
  import * as d3 from "d3";
  import { scaleLinear } from "d3-scale";
  import { Guatemala2 } from "../data_gdp/Guatemala2";
  import { Honduras2 } from "../data_gdp/Honduras2";
  import { Colombia2 } from "../data_gdp/Colombia2";

  export let data = [];

  let g = false;
  let h = false;
  let c = false;
  let choice;

  let chartWidth = 1200;
  let chartHeight = 600;

  const paddings = {
    top: 40,
    left: 200,
    right: 100,
    bottom: 100,
  };

  function chooseG() {
    choice = "Guatemala";
    g = true;
    h = false;
    c = false;
    data = [];
    Guatemala2.forEach((element) =>
      data.push({
        index: element["Year"],
        size: element["Change"],
      })
    );
    console.log("Guatemala");
  }

  function chooseH() {
    choice = "Honduras";
    g = false;
    h = true;
    c = false;
    data = [];
    Honduras2.forEach((element) =>
      data.push({
        index: element["Year"],
        size: element["Change"],
      })
    );
    console.log("Honduras");
  }

  function chooseC() {
    choice = "Colombia";
    g = false;
    h = false;
    c = true;
    data = [];
    Colombia2.forEach((element) =>
      data.push({
        index: element["Year"],
        size: element["Change"],
      })
    );
    console.log("Colombia");
  }

  const margin = { top: 15, bottom: 50, left: 50, right: 20 };

  const innerHeight = chartHeight - margin.top - margin.bottom,
    innerWidth = chartWidth - margin.left - margin.right;

  // set scaling variables
  $: xScale = scaleLinear()
    .domain([
      Math.min(...data.map((d) => d.index)),
      Math.max(...data.map((d) => d.index)),
    ])
    .range([paddings.left, chartWidth - paddings.right]);
  $: yScale = scaleLinear()
    .domain([
      Math.min(...data.map((d) => d.size)),
      Math.max(...data.map((d) => d.size)),
    ])
    .range([chartHeight - paddings.bottom, paddings.top]);

  let xTicks = [];
  let yTicks = [];
  let numTicks = 5;
  $: {
    xTicks = [];
    yTicks = [];

    if (data.length > 1) {
      let index_extent = [
        Math.round(Math.min(...data.map((d) => d.index))),
        Math.round(Math.max(...data.map((d) => d.index)) + 1),
      ];
      let index_increment = Math.floor(
        (index_extent[1] - index_extent[0]) / numTicks
      );
      for (
        let i = index_extent[0];
        i < index_extent[1];
        i = i + Math.max(1, index_increment)
      ) {
        xTicks.push(i);
      }

      let size_extent = [
        Math.round(Math.min(...data.map((d) => d.size))),
        Math.round(Math.max(...data.map((d) => d.size)) + 1),
      ];
      let size_increment = Math.floor(
        (size_extent[1] - size_extent[0]) / numTicks
      );
      for (
        let i = size_extent[0];
        i < size_extent[1];
        i = i + Math.max(1, size_increment)
      ) {
        yTicks.push(i);
      }
    }
  }

  const idContainer = "svg-container-" + Math.random() * 1000000;
  let mousePosition = { x: null, y: null };
  let pageMousePosition = { x: null, y: null };
  let currentHoveredPoint = null;

  function followMouse(event) {
    const svg = document.getElementById(idContainer);
    if (svg === null) return;
    const dim = svg.getBoundingClientRect();
    pageMousePosition = {
      x: event.pageX,
      y: event.pageY,
    };
    const positionInSVG = {
      x: event.clientX - dim.left,
      y: event.clientY - dim.top,
    };
    mousePosition =
      positionInSVG.x > paddings.left &&
      positionInSVG.x < chartWidth - paddings.right &&
      positionInSVG.y > paddings.top &&
      positionInSVG.y < chartHeight - paddings.bottom
        ? { x: positionInSVG.x, y: positionInSVG.y }
        : { x: null, y: null };
  }
  function removePointer() {
    mousePosition = { x: null, y: null };
  }
  function computeSelectedXValue(value) {
    currentHoveredPoint =
      data[data.indexOf(data.filter((d) => xScale(d.index) >= value)[0]) - 1];
    return data.filter((d) => xScale(d.index) >= value)[0].index - 1;
  }
</script>

<div class="percent">
  {#if data.length > 1}
    <svg
      width={chartWidth}
      height={chartHeight}
      on:mousemove={followMouse}
      on:mouseleave={removePointer}
      id={idContainer}
    >
      <g>
        <line
          x1={paddings.left}
          x2={chartWidth - paddings.right}
          y1={chartHeight - paddings.bottom}
          y2={chartHeight - paddings.bottom}
          stroke="#6e3003"
          stroke-width="2"
          class="axis"
        />
        <line
          x1={paddings.left}
          x2={paddings.left}
          y1={chartHeight - paddings.bottom}
          y2={paddings.top}
          stroke="#6e3003"
          stroke-width="2"
          class="axis"
        />
        <text transform={`translate(${30},${innerHeight / 2}) rotate(-90)`}
          >Percent of GDP</text
        >
        <text x={innerWidth / 2} y={innerHeight + 35}>Year</text>
      </g>

      <g>
        {#each data as d, i}
          {#if i != data.length - 1}
            <line
              x1={xScale(data[i].index)}
              x2={xScale(data[i + 1].index)}
              y1={yScale(data[i].size)}
              y2={yScale(data[i + 1].size)}
              stroke="#b86a04"
              stroke-width="2"
            />
          {/if}
        {/each}
      </g>

      <g transform="translate(0, {chartHeight - paddings.bottom})">
        {#each xTicks as x}
          <g class="tick" opacity="1" transform="translate({xScale(x)},0)">
            <line stroke="#6e3003" y2="6" />
            <text dy="0.71em" fill="#6e3003" y="10" x="-5" text-anchor="middle">
              {x}
            </text>
          </g>
        {/each}
      </g>
      <g transform="translate({paddings.left}, 0)">
        {#each yTicks as y}
          <g class="tick" opacity="1" transform="translate(0,{yScale(y)})">
            <line stroke="#6e3003" x2="-5" />
            <text dy="0.32em" fill="#6e3003" x="-{10}" text-anchor="end">
              {y}
            </text>
          </g>
        {/each}
      </g>

      <g>
        {#each data as d, i}
          {#if i != data.length - 1}
            <line
              x1={xScale(data[i].index)}
              x2={xScale(data[i + 1].index)}
              y1={yScale(data[i].size)}
              y2={yScale(data[i + 1].size)}
              stroke="#b86a04"
              stroke-width="2"
            />
          {/if}
        {/each}
      </g>

      {#if mousePosition.x !== null}
        <g
          transform="translate({xScale(
            computeSelectedXValue(mousePosition.x)
          )} 0)"
        >
          <line
            x1="0"
            x2="0"
            y1={paddings.top}
            y2={chartHeight - paddings.bottom - 2}
            stroke="black"
            stroke-width="1"
          />
          <circle
            cx={0}
            cy={yScale(
              data.find(
                (d) => d.index === computeSelectedXValue(mousePosition.x)
              ).size
            )}
            r="3"
            fill="#b86a04"
          />
        </g>
      {/if}
    </svg>
    <div
      class={mousePosition.x === null ? "tooltip-hidden" : "tooltip-visible"}
      style="left: {mousePosition.x + 10}px; top: {mousePosition.y + 10}px"
    >
      {#if mousePosition.x !== null}
        In the year {currentHoveredPoint.index}, the net migration in {choice} was
        {Math.round(currentHoveredPoint.size * 100) / 100}.
      {/if}
    </div>
  {:else}
    <p>Select a country...</p>
  {/if}
  <section class="buttons">
    <button class:g on:click={() => chooseG()}>Guatemala</button>
    <button class:h on:click={() => chooseH()}>Honduras</button>
    <button class:c on:click={() => chooseC()}>Colombia</button>
  </section>
</div>

<style>
  .visualization {
    font: 25px sans-serif;
    margin: auto;
    margin-top: 1px;
    text-align: middle;
  }

  /* dynamic classes for the tooltip */
  .tooltip-hidden {
    visibility: hidden;
    font-family: "Nunito", sans-serif;
    width: 200px;
    position: absolute;
  }

  .tooltip-visible {
    font: 25px sans-serif;
    font-family: "Nunito", sans-serif;
    visibility: visible;
    background-color: #f0dba8;
    border-radius: 10px;
    width: 200px;
    color: black;
    position: absolute;
    padding: 10px;
  }
  .axis {
    stroke-linejoin: round;
    stroke-dasharray: 4400;
    stroke-dashoffset: 0;
    animation: draw 8.5s ease;
  }
  @keyframes draw {
    from {
      stroke-dashoffset: 4400;
    }
    to {
      stroke-dashoffset: 0;
    }
  }

  .g {
    background-color: gray;
  }
  .h {
    background-color: gray;
  }
  .c {
    background-color: gray;
  }
</style>
