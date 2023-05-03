<script>
  import ChartGDP from "../components/chart_gdp.svelte";
  import ChartImm from "../components/chart_imm.svelte";

  /**
   * @type {never[]}
   */
  let data = [];

  let currentChart = "";

  const toggleChart = (/** @type string */ chart) => {
    // document.getElementById('chart-container').
    if (currentChart == "") {
      currentChart = chart;
    } else {
      currentChart = "";
    }
  };
</script>

<main>
  <div id="buttons-container">
    <button
      class={currentChart == "" ? "button" : "hidden"}
      on:click={() => toggleChart("gdp")}
      >{currentChart === "gdp" ? "Hide GDP Graph" : "View GDP Graph"}</button
    >
    <button
      class={currentChart == "" ? "button" : "hidden"}
      on:click={() => toggleChart("imm")}
      >{currentChart === "imm"
        ? "Hide Migration Graph"
        : "View Migration Graph"}</button
    >
    <button
      class={currentChart != "" ? "button" : "hidden"}
      on:click={() => toggleChart("gdp")}>Hide Graph</button
    >
  </div>
  <div class={currentChart == "gdp" ? "chart-container-selected" : "hidden"}>
    <h1>Percent of GDP</h1>
    <section class="graph">
      <ChartGDP bind:data />
    </section>
  </div>
  <div class={currentChart == "imm" ? "chart-container-selected" : "hidden"}>
    <h1>Net Migration</h1>
    <section class="graph">
      <ChartImm bind:data />
    </section>
  </div>
</main>

<style>
  main {
    text-align: center;
    font-family: "Nunito", sans-serif;
    font-weight: 300;
    line-height: 2;
    font-size: 24px;
    color: var(--color-text);
    margin-top: 100px;
  }

  #buttons-container {
    border-style: solid;
    background-color: #3a405a;
    width: 100%;
    height: 100px;
    position: fixed;
    bottom: 0;
    right: 0;
    display: flex;
    justify-content: space-around;
    padding-top: 10px;
    padding-bottom: 10px;
  }

  .button {
    padding: 30px;
    border-radius: 45px;
    font-size: large;
    font-weight: bold;
    background-color: #aec5eb;
    color: #e9afa3;
    color: #3a405a;
  }

  .chart-container-selected {
    border-style: solid;
    background-color: #aec5eb;
    width: 100%;
    height: 890px;
    position: fixed;
    top: 0;
    left: 0;
  }

  .hidden {
    display: none;
  }

  .graph {
    display: inline-block;
    margin-left: 50px;
  }
</style>
