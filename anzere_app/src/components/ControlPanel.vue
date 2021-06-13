<template>
  <div class="control-panel">
    <img id="logo" src="/images/anzere.png"/>
    <table>
      <tr>
        <td>Pistes</td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.PISTES, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Telecabines</td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.TELECABINES, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Chair-Lifts</td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.CHAIRLIFTS, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Ski-Lifts</td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.SKILIFTS, $event.target.checked) " checked></td>
      </tr>
      <tr>
        <td>Stations</td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.STATIONS, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Restaurants & Bars</td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.COMMERCE, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Parking</td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.PARKING, $event.target.checked)" checked></td>
      </tr>
    </table>
  </div>
</template>

<script>
import { EventBus } from '../main'
import { EVENTS } from '../constants'

export default {
  name: "ControlPanel",
  data() {
    return {
      BUS: EventBus,
      EVENTS: EVENTS
    }
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
