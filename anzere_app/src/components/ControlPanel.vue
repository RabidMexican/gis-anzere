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
    <div class="slider-wrapper">
      <div class="divider"/>
    </div>
    <div class='traffic-wrapper'>
      <label>Toggle traffic
        <input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE_TRAFFIC, $event.target.checked)" v-model="showTraffic">
      </label>
    </div>
    <div class="slider-wrapper">
       <input type="range" id="slider" name="time" min="0" max="9" list="tickmarks" v-model="hour" @change="BUS.$emit(EVENTS.TIME, hour)" :disabled="!showTraffic">
       <datalist id="tickmarks">
        <option value="0" label="hello"></option>
        <option value="1"></option>
        <option value="2"></option>
        <option value="3"></option>
        <option value="4" label="12:00"></option>
        <option value="5"></option>
        <option value="6"></option>
        <option value="7"></option>
        <option value="8"></option>
        <option value="9" label = "17:00"></option>
      </datalist>
    </div>
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
      EVENTS: EVENTS,
      hour: 0,
      showTraffic: false,
    }
  }
}
</script>

<style scoped>
  .traffic-wrapper {
    text-align: left;
    margin-bottom: 1rem;
  }
  .divider {
    width: 90%;
    border-top: 1px solid #d6d6d6;
    margin: 20px auto;
  }
  #slider { width:80% }
  .slider-wrapper { text-align: center }
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
