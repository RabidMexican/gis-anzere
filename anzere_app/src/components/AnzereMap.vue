<template>
  <div id="map-container">
    <LMap :zoom="zoom" :center="center">

      <div class="background"/>
      <LTileLayer :url="url"/>

      <!-- USER LOCATION -->
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

      <!-- PISTES -->
      <LPolyline
          v-for="piste in pistes"
          v-bind:key="'PI' + piste.properties.pk"
          :visible="pistes_visible"
          :color="getPisteColor(piste.properties.difficulty)"
          :lat-lngs="getLineCoords(piste.geometry.coordinates)">
        <LPopup>
          <PopupPiste
              :name="piste.properties.name"
              :difficulty="piste.properties.difficulty"/>
        </LPopup>
      </LPolyline>

      <!-- PARKING -->
      <LPolygon
          v-for="parking in parkings"
          v-bind:key="'PK' + parking.properties.pk"
          :visible="parking_visbile"
          :lat-lngs="getPolyCoords(parking.geometry.coordinates)">
        <LPopup>
          <PopupParking 
              :name="parking.properties.name"
              :capacity="parking.properties.nb_place"
              :free="parking.properties.free"/>
        </LPopup>
      </LPolygon>

      <!-- COMMERCE -->
      <LPolygon
          v-for="shop in commerce"
          v-bind:key="'SH' + shop.properties.pk"
          :visible="commerce_visible"
          :lat-lngs="getPolyCoords(shop.geometry.coordinates)">
        <LPopup>
          <PopupCommerce 
              :name="shop.properties.name"
              :type="shop.properties.type"
              :places="shop.properties.nb_place"/>
        </LPopup>
      </LPolygon>

      <!-- STATIONS -->
      <LPolygon
          v-for="station in stations"
          v-bind:key="'ST' + station.properties.pk"
          :visible="stations_visible"
          :lat-lngs="getPolyCoords(station.geometry.coordinates)">
        <LPopup>
          <PopupStation :name="station.properties.name"/>
        </LPopup>
      </LPolygon>

      <!-- TELECABINES -->
      <LPolyline
          v-for="telecabine in telecabines"
          v-bind:key="'T' + telecabine.properties.pk"
          :visible="telecabines_visible"
          :lat-lngs="getLineCoords(telecabine.geometry.coordinates)">
        <LPopup>
          <PopupTelecabine :name="telecabine.properties.name"/>
        </LPopup>
      </LPolyline>

      <!-- CHAIRLIFTS -->
      <LPolyline
          v-for="clift in chairlifts"
          v-bind:key="'CL' + clift.properties.pk"
          :visible="chairlifts_visible"
          :lat-lngs="getLineCoords(clift.geometry.coordinates)">
        <LPopup>
          <PopupChairlift :name="clift.properties.name"/>
        </LPopup>
      </LPolyline>

      <!-- SKILIFTS -->
      <LPolyline
          v-for="slift in skilifts"
          v-bind:key="'SL' + slift.properties.pk"
          :visible="skilifts_visible"
          :lat-lngs="getLineCoords(slift.geometry.coordinates)">
        <LPopup>
          <PopupSkilift :name="slift.properties.name"/>
        </LPopup>
      </LPolyline>

    </LMap>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup, LPolygon, LIcon, LPolyline } from 'vue2-leaflet'
import PopupParking from './popups/PopupParking'
import PopupPiste from './popups/PopupPiste'
import PopupCommerce from './popups/PopupCommerce'
import PopupStation from './popups/PopupStation'
import PopupTelecabine from './popups/PopupTelecabine'
import PopupChairlift from './popups/PopupCharlift'
import PopupSkilift from './popups/PopupSkilift'
import { EventBus } from '../main'
import axios from 'axios'
import API from '../constants'

export default {
  name: "Map",
  components: {
    PopupParking,
    PopupPiste,
    PopupCommerce,
    PopupStation,
    PopupTelecabine,
    PopupChairlift,
    PopupSkilift,
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LPolygon,
    LPolyline,
    LIcon
  },
  data() {
    return {
      position: {
        latitude: 0,
        longitude: 0,
      },

      url: "https://{s}.tile.osm.org/{z}/{x}/{y}.png",
      zoom: 14,
      center: [46.3164, 7.4048],

      parkings: [],
      parking_visbile: true,

      pistes: [],
      pistes_visible: true,

      commerce: [],
      commerce_visible: true,

      stations: [],
      stations_visible: true,

      telecabines: [],
      telecabines_visible: true,

      chairlifts: [],
      chairlifts_visible: true,

      skilifts: [],
      skilifts_visible: true,
    }
  },
  created (){
    EventBus.$on('toggle_pistes',      (data) => { this.pistes_visible = data } )
    EventBus.$on('toggle_telecabines', (data) => { this.telecabines_visible = data })
    EventBus.$on('toggle_clifts',      (data) => { this.chairlifts_visible = data })
    EventBus.$on('toggle_slifts',      (data) => { this.skilifts_visible = data })
    EventBus.$on('toggle_stations',    (data) => { this.stations_visible = data })
    EventBus.$on('toggle_commerce',    (data) => { this.commerce_visible = data })
    EventBus.$on('toggle_parking',     (data) => { this.parking_visbile = data })
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
.background {
  width: 100%;
  height: 100%;
  background-color: white;
}
</style>