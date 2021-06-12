<template>
  <div class="control-panel">
    <img id="logo" src="/images/anzere.png"/>
    <table>
      <tr>
        <td>Pistes</td>
        <td><input type="checkbox" @change="togglePistes($event)" checked></td>
      </tr>
      <tr>
        <td>Telecabines</td>
        <td><input type="checkbox" @change="toggleTelecabines($event)" checked></td>
      </tr>
      <tr>
        <td>Chair-Lifts</td>
        <td><input type="checkbox" @change="toggleChairlifts($event)" checked></td>
      </tr>
      <tr>
        <td>Ski-Lifts</td>
        <td><input type="checkbox" @change="toggleSkilifts($event)" checked></td>
      </tr>
      <tr>
        <td>Stations</td>
        <td><input type="checkbox" @change="toggleStations($event)" checked></td>
      </tr>
      <tr>
        <td>Restaurants & Bars</td>
        <td><input type="checkbox" @change="toggleCommerce($event)" checked></td>
      </tr>
      <tr>
        <td>Parking</td>
        <td><input type="checkbox" @change="toggleParking($event)" checked></td>
      </tr>
    </table>
  </div>
</template>

<script>
import { EventBus } from '../main'

export default {
  name: "ControlPanel",
  methods: {
    togglePistes:       (event) => { EventBus.$emit('toggle_pistes', event.target.checked) },
    toggleTelecabines:  (event) => { EventBus.$emit('toggle_telecabines', event.target.checked) },
    toggleChairlifts:   (event) => { EventBus.$emit('toggle_clifts', event.target.checked) },
    toggleSkilifts:     (event) => { EventBus.$emit('toggle_slifts', event.target.checked) },
    toggleStations:     (event) => { EventBus.$emit('toggle_stations', event.target.checked) },
    toggleCommerce:     (event) => { EventBus.$emit('toggle_commerce', event.target.checked) },
    toggleParking:      (event) => { EventBus.$emit('toggle_parking', event.target.checked) },
  }
}
</script>

<style scoped>
  #logo { width: 20rem }
  .control-panel {
    text-align: right;
    position: absolute;
    top: 0;
    right: 0;
    z-index: 999;
    margin: 1rem;
    padding: 2rem;
    border-radius: 8px;
    background-color: white;
    box-shadow: 0 3px 14px rgb(0 0 0 / 40%);
  }
  table { 
    margin-top: 2rem;
    margin-left: auto;
  }
  tr td:first-child { padding-right: 1rem }
</style>
