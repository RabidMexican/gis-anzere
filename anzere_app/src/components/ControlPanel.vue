<template>
  <div class="control-panel">
    <img id="logo" src="/images/anzere.png"/>
    <table>
      <tr>
        <td>Pistes</td>
        <td></td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.PISTES, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Telecabines</td>
         <td><div class="key-circle" :style="'background-color: ' + COLORS.TELECABINES"></div></td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.TELECABINES, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Chair-Lifts</td>
        <td><div class="key-circle" :style="'background-color: ' + COLORS.CHAIRLIFTS"></div></td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.CHAIRLIFTS, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Ski-Lifts</td>
        <td><div class="key-circle" :style="'background-color: ' + COLORS.SKILIFTS"></div></td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.SKILIFTS, $event.target.checked) " checked></td>
      </tr>
      <tr>
        <td>Stations</td>
        <td><div class="key-circle" :style="'background-color: ' + COLORS.STATIONS"></div></td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.STATIONS, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Restaurants & Bars</td>
         <td><div class="key-circle" :style="'background-color: ' + COLORS.COMMERCE"></div></td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.COMMERCE, $event.target.checked)" checked></td>
      </tr>
      <tr>
        <td>Parking</td>
        <td><div class="key-circle" :style="'background-color: ' + COLORS.PARKING"></div></td>
        <td><input type="checkbox" @change="BUS.$emit(EVENTS.TOGGLE.PARKING, $event.target.checked)" checked></td>
      </tr>
    </table>
    <div class="slider-wrapper">
      <div class="divider"/>
    </div>
    <div class='traffic-wrapper'>
      <label>Show traffic
        <input type="checkbox" style="margin-left: 1rem" @change="BUS.$emit(EVENTS.TOGGLE_TRAFFIC, $event.target.checked)" v-model="showTraffic">
      </label>
      <button @click="playPause()" :disabled="!showTraffic">
        <img :src="'/images/icons/' + playIcon + '.svg'" />
      </button>
    </div>
    <div class="slider-wrapper">
      <input type="range" id="slider" name="time" min="0" max="18" list="hour" v-model="hour" @change="BUS.$emit(EVENTS.TIME, hour)" :disabled="!showTraffic">
      <div class="slider-time">
        <div>8:00</div>
        <div>12:00</div>
        <div>17:00</div>
      </div>
      <datalist id="hour">
        <option value="0"></option>
        <option value="1"></option>
        <option value="2"></option>
        <option value="3"></option>
        <option value="4"></option>
        <option value="5"></option>
        <option value="6"></option>
        <option value="7"></option>
        <option value="8"></option>
        <option value="9"></option>
        <option value="10"></option>
        <option value="11"></option>
        <option value="12"></option>
        <option value="13"></option>
        <option value="14"></option>
        <option value="15"></option>
        <option value="16"></option>
        <option value="17"></option>
        <option value="18"></option>
      </datalist>
    </div>
  </div>
</template>

<script>
import { EventBus } from '../main'
import { EVENTS, MAX_HOUR, COLORS } from '../constants'

export default {
  name: "ControlPanel",
  data() {
    return {
      BUS: EventBus,
      EVENTS: EVENTS,
      COLORS: COLORS,
      MAX_HOUR: MAX_HOUR,
      hour: 0,
      showTraffic: false,
      playIcon: 'play',
      playStatus: false,
      playInstance: null,
    }
  },
  methods: {
    playPause() {
      if(this.hour == this.MAX_HOUR) this.restart()
      else if(this.playStatus) this.pause()
      else this.play()
    },
    play() {
      this.playStatus = true
      this.playIcon = 'pause'
      let playState = window.setInterval(() => {
        if (!this.playStatus) clearInterval(playState)
        this.hour++
        this.BUS.$emit(EVENTS.TIME, this.hour)
        if (this.hour == this.MAX_HOUR) {
          this.playIcon = 'refresh'
          clearInterval(playState)
        }
      }, 800) // 0.8 seconds gaps
    },
    pause() {
      this.playStatus = false
      this.playIcon = 'play'
    },
    restart() {
      this.hour = 0
      this.play()
    }
  }
}
</script>

<style scoped>
  .slider-time {
    display: flex;
    justify-content: space-between;
    padding: 0 30px;
    font-size: 0.8rem;
    color: #00000079;
  }
  .traffic-wrapper {
    display: flex;
    justify-content: space-between;
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
  tr td:nth-child(2) { width: 1rem }
  tr td:nth-child(1) { padding-right: 1rem }
  .key-circle {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    border: 2px solid black;
  }
</style>
