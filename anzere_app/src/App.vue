<template>
  <div id="app">
    <ControlPanel/>
    <Map
      v-if="loaded"
      :parkings="parkings"
      :pistes="pistes"
      :commerce="commerce"
      :stations="stations"
      :telecabines="telecabines"
      :chairlifts="chairlifts"
      :skilifts="skilifts"
    />
  </div>
</template>

<script>
import { API } from './constants'
import Map from './components/AnzereMap.vue'
import ControlPanel from './components/ControlPanel.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Map,
    ControlPanel,
  },
  data() {
    return {
      loaded: false,
      parkings: null,
      pistes: null,
      commerce: null,
      stations: null,
      telecabines: null,
      chairlifts: null,
      skilifts: null,
    }
  },
  async mounted() {
        // Get all data
    await axios.get(API + 'parking/all')
      .then((response) => { this.parkings = response.data.features })
    await axios.get(API + 'piste/all')
      .then((response) => { this.pistes = response.data.features })
    await axios.get(API + 'commerce/all')
      .then((response) => { this.commerce = response.data.features })
    await axios.get(API + 'gare/all')
      .then((response) => { this.stations = response.data.features })
    await axios.get(API + 'telecabine/all')
      .then((response) => { this.telecabines = response.data.features })
    await axios.get(API + 'telesiege/all')
      .then((response) => { this.chairlifts = response.data.features })
    await axios.get(API + 'teleski/all')
      .then((response) => { this.skilifts = response.data.features })

    this.loaded = true
  }
}
</script>

<style>
  body {
    margin: 0;
    font-family: 'Open Sans', sans-serif;
  }
</style>
