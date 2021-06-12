<template>
  <div id="map-container">
    <LMap :zoom="zoom" :center="center" :options="mapOptions">

      <LTileLayer :url="url"/>

      <LMarker
          v-if="position"
          name="You are here!"
          :lat-lng="[position.latitude, position.longitude]">
        <LIcon 
            icon-url="/images/location.png"
            :icon-size="[50, 50]"
            :icon-anchor="[25, 45]"/>
        <LPopup content="You are here!"/>
      </LMarker>

      <LPolyline
          v-for="piste in pistes"
          v-bind:key="'PI' + piste.properties.pk"
          :color="getPisteColor(piste.properties.difficulty)"
          :lat-lngs="getLineCoords(piste.geometry.coordinates)">
        <LPopup>
          <PopupPiste
              :name="piste.properties.name"
              :difficulty="piste.properties.difficulty"/>
        </LPopup>
      </LPolyline>

      <LPolygon
          v-for="parking in parkings"
          v-bind:key="'PK' + parking.properties.pk"
          :lat-lngs="getPolyCoords(parking.geometry.coordinates)">
        <LPopup>
          <PopupParking 
              :name="parking.properties.name"
              :capacity="parking.properties.nb_place"
              :free="parking.properties.free"/>
        </LPopup>
      </LPolygon>

      <LPolygon
          v-for="shop in commerce"
          v-bind:key="'SH' + shop.properties.pk"
          :lat-lngs="getPolyCoords(shop.geometry.coordinates)">
        <LPopup>
        </LPopup>
      </LPolygon>

      <!--LGeoJson
          v-for="shop in commerce"
          v-bind:key="'SH' + shop.properties.pk"
          :geojson="shop.geometry"/-->

      <LGeoJson
          v-for="station in stations"
          v-bind:key="'S' + station.properties.pk"
          :geojson="station.geometry"/>

      <LGeoJson
          :options="opt_telecabine"
          v-for="telecabine in telecabines"
          v-bind:key="'T' + telecabine.properties.pk"
          :geojson="telecabine.geometry"/>

      <LGeoJson
          :options="opt_charlift"
          v-for="clift in chairlifts"
          v-bind:key="'CL' + clift.properties.pk"
          :geojson="clift.geometry"/>

      <LGeoJson
          v-for="slift in skilifts"
          v-bind:key="'SL' + slift.properties.pk"
          :geojson="slift.geometry"/>

    </LMap>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LGeoJson, LPopup, LPolygon, LIcon, LPolyline } from 'vue2-leaflet'
import PopupParking from './popups/PopupParking.vue'
import PopupPiste from './popups/PopupPiste.vue'
import axios from 'axios'
import API from '../constants'
export default {
  name: "Map",
  components: {
    PopupParking,
    PopupPiste,
    LMap,
    LTileLayer,
    LMarker,
    LGeoJson,
    LPopup,
    LPolygon,
    LPolyline,
    LIcon,
  },
  data() {
    return {
      position: {
        latitude: 0,
        longitude: 0,
      },
      parkings: [],
      pistes: [],
      commerce: [],
      passages: [],
      stations: [],
      telecabines: [],
      chairlifts: [],
      skilifts: [],
      url: "https://{s}.tile.osm.org/{z}/{x}/{y}.png",
      zoom: 14,
      center: [46.3164, 7.4048], // Telecabine
      bounds: null,
      opt_charlift: {
        color: "darkblue"
      },
      opt_skilift: {
        color: "red"
      },
      opt_parking: {
        color: "purple",
        fillOpacity: 0.5,
      },
       opt_telecabine: {
        color: "green"
      },
      mapOptions: {
        onEachFeature: function onEachFeature(feature, layer) {
          layer.bindPopup("Id is " + feature.properties.id);
        }
      }
    }
  },
  async mounted() {
    // Get location
    this.getLocation()

    // Get all data
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
    await axios.get(API + 'gare/all')
      .then((response) => { 
        this.stations = response.data.features
      })
    await axios.get(API + 'telecabine/all')
      .then((response) => { 
        this.telecabines = response.data.features
      })
    await axios.get(API + 'telesiege/all')
      .then((response) => { 
        this.chairlifts = response.data.features
      })
    await axios.get(API + 'teleski/all')
      .then((response) => { 
        this.skilifts = response.data.features
      })
  },
  methods: {
    getLocation() {
       if(navigator.geolocation) {
          navigator.geolocation.getCurrentPosition(this.updateLocation);
      }
    },
    updateLocation(position) {
      this.position.latitude = position.coords.latitude;
      this.position.longitude = position.coords.longitude;
    },
    getPisteColor (diff) { 
      switch(diff) {
        case 1: return 'green'
        case 2: return 'blue'
        case 3: return 'red'
        case 4: return 'black'
      }
    },
    getPolyCoords(geojson) {
      let result = []
      geojson.forEach((top) => {
        top.forEach((middle) => {
          middle.forEach((bottom) => {
            bottom = new Array(bottom[1], bottom[0])
            result.push(bottom)
          })
        })
      })
      console.log(result)
      return result
    },
     getLineCoords(geojson) {
      let result = []
      geojson.forEach((top) => {
          top.forEach((bottom) => {
            bottom = new Array(bottom[1], bottom[0])
            result.push(bottom)
          })
      })
      return result
    }
  },
}
</script>

<style scoped>
#map-container {
  height: 100vh
}
</style>