<template>
  <div id="map-container">
    <LMap :zoom="zoom" :center="center">
      <LTileLayer :url="url"></LTileLayer>
      <LMarker :lat-lng="[46.29521, 7.39499]"></LMarker>
      <LGeoJson
          v-for="parking in parkings"
          v-bind:key="parking.properties.nom"
          :geojson="parking.geometry"/>
      <LGeoJson 
          :options="options"
          v-for="piste in pistes"
          v-bind:key="piste.properties.nom"
          :geojson="piste.geometry"/>
      <LGeoJson
          v-for="shop in commerce"
          v-bind:key="shop.properties.nom"
          :geojson="shop.geometry"/>
      <LGeoJson
          v-for="passage in passages"
          v-bind:key="passage.properties.nom"
          :geojson="passage.geometry"/>
      <LGeoJson
          v-for="station in stations"
          v-bind:key="station.properties.nom"
          :geojson="station.geometry"/>
    </LMap>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LGeoJson } from "vue2-leaflet";
import axios from 'axios'
import API from '../constants'
export default {
  name: "Map",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LGeoJson
  },
  data() {
    return {
      parkings: [],
      pistes: [],
      commerce: [],
      passages: [],
      stations: [],
      url: "https://{s}.tile.osm.org/{z}/{x}/{y}.png",
      zoom: 16,
      center: [46.29521, 7.39499], // Telecabine
      bounds: null,
      options: {
        color: "red"
      }
    };
  },
  async mounted() {
    await axios.get(API + 'parking/all')
      .then((response) => { 
        this.parkings = response.data.features
      })
    await axios.get(API + 'piste/all')
      .then((response) => { 
        this.pistes = response.data.features
      })
    await axios.get(API + 'commerce/all')
    .then((response) => { 
      this.commerce = response.data.features
    })
    await axios.get(API + 'passage/all')
    .then((response) => { 
      this.passages = response.data.features
    })
    await axios.get(API + 'gare/all')
    .then((response) => { 
      this.stations = response.data.features
    })
  }
}
</script>

<style scoped>
#map-container {
  height: 100vh
}
</style>