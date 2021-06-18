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
          :visible="loaded && pistes_visible"
          :color="showTraffic ? getColorForHour(piste, time) : getPisteColor(piste.properties.difficulty)"
          :lat-lngs="getLineCoords(piste.geometry.coordinates)">
        <LPopup>
          <PopupPiste
              :name="piste.properties.name"
              :difficulty="piste.properties.difficulty"/>
        </LPopup>
      </LPolyline>
      <!--:color="getPisteColor(piste.properties.difficulty)"-->

      <!-- PARKING -->
      <LPolygon
          v-for="parking in parkings"
          v-bind:key="'PK' + parking.properties.pk"
          :visible="loaded && parking_visbile"
           :color="showTraffic ? getColorForHour(parking, time) : '#9c9c9c'"
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
          :color="showTraffic ? getColorForHour(shop, time) : '#854ccf'"
          :visible="loaded && commerce_visible"
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
          :visible="loaded && stations_visible"
          :color="showTraffic ? getColorForHour(station, time) : '#1fbf54'"
          :lat-lngs="getPolyCoords(station.geometry.coordinates)">
        <LPopup>
          <PopupStation :name="station.properties.name"/>
        </LPopup>
      </LPolygon>

      <!-- TELECABINES -->
      <LPolyline
          v-for="telecabine in telecabines"
          :color="showTraffic ? getColorForHour(telecabine, time) : '#22a6d6'"
          v-bind:key="'T' + telecabine.properties.pk"
          :visible="loaded && telecabines_visible"
          :lat-lngs="getLineCoords(telecabine.geometry.coordinates)">
        <LPopup>
          <PopupTelecabine :name="telecabine.properties.name"/>
        </LPopup>
      </LPolyline>

      <!-- CHAIRLIFTS -->
      <LPolyline
          v-for="clift in chairlifts"
          v-bind:key="'CL' + clift.properties.pk"
          :visible="loaded && chairlifts_visible"
          :color="showTraffic ? getColorForHour(clift, time) : '#03a600'"
          :lat-lngs="getLineCoords(clift.geometry.coordinates)">
        <LPopup>
          <PopupChairlift :name="clift.properties.name"/>
        </LPopup>
      </LPolyline>

      <!-- SKILIFTS -->
      <LPolyline
          v-for="slift in skilifts"
          v-bind:key="'SL' + slift.properties.pk"
          :visible="loaded && skilifts_visible"
          :color="showTraffic ? getColorForHour(slift, time) : '#cadb0d'"
          :lat-lngs="getLineCoords(slift.geometry.coordinates)">
        <LPopup>
          <PopupSkilift :name="slift.properties.name"/>
        </LPopup>
      </LPolyline>

    </LMap>
  </div>
</template>

<script>
import { API, EVENTS } from '../constants'
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

      loaded: false,
      busy: [0,0,0,0,0,0,0,0,0,0,],
      percentColors : [
        { pct: 0.0, color: { r: 0xff, g: 0x00, b: 0 } },
        { pct: 0.5, color: { r: 0xff, g: 0xff, b: 0 } },
        { pct: 1.0, color: { r: 0x00, g: 0xff, b: 0 } } 
      ],

      time: 0,
      showTraffic: false,

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
    // Add listeners for filters
    EventBus.$on(EVENTS.TOGGLE.PISTES,      (state) => { this.pistes_visible = state } )
    EventBus.$on(EVENTS.TOGGLE.TELECABINES, (state) => { this.telecabines_visible = state })
    EventBus.$on(EVENTS.TOGGLE.CHAIRLIFTS,  (state) => { this.chairlifts_visible = state })
    EventBus.$on(EVENTS.TOGGLE.SKILIFTS,    (state) => { this.skilifts_visible = state })
    EventBus.$on(EVENTS.TOGGLE.STATIONS,    (state) => { this.stations_visible = state })
    EventBus.$on(EVENTS.TOGGLE.COMMERCE,    (state) => { this.commerce_visible = state })
    EventBus.$on(EVENTS.TOGGLE.PARKING,     (state) => { this.parking_visbile = state })
    EventBus.$on(EVENTS.TIME,               (time) =>  { this.time = time})
    EventBus.$on(EVENTS.TOGGLE_TRAFFIC,     (state) => { this.showTraffic = state })
  },
  async mounted() {
    // Get location of user
    this.getLocation()

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
    
    await this.getBuisiestHour()

    this.loaded = true

    this.getColorForHour(this.parkings[0], 0)
  },
  methods: {
    // Get location of user
    getLocation() {
      if(navigator.geolocation) 
        navigator.geolocation.getCurrentPosition(this.updateLocation)
    },
    // Update data with poisition
    updateLocation(position) {
      this.position.latitude = position.coords.latitude;
      this.position.longitude = position.coords.longitude;
    },
    // Gets the buisiest hour
    async getBuisiestHour() {
      for(let i = 0; i < this.busy.length; i++) {
        this.busy[i] =  Math.max(...[
          this.getBuisiestForHour(this.parkings, i),
          this.getBuisiestForHour(this.pistes, i),
          this.getBuisiestForHour(this.commerce, i),
          this.getBuisiestForHour(this.stations, i),
          this.getBuisiestForHour(this.telecabines, i),
          this.getBuisiestForHour(this.chairlifts, i),
          this.getBuisiestForHour(this.skilifts, i),
        ])
      }
    },
    // Gets busiest hour for object for given hour
    getBuisiestForHour(objs, hour) {
      let max = 0
      const attr = 't_' + hour
      objs.forEach((obj) => {
        let current = obj.properties[attr]
        if(current > max) max = current
      })
      return max
    },
    // Gets the color for an object for given hour
    getColorForHour(obj, hour) {
      let attr = 't_' + hour
      let value = obj.properties[attr]
      if(value == 0) return this.getColor(0.000001)
      return this.getColor(value / this.busy[hour])
    },
    // Translates the comparison to busiest hour into a color
    getColor(value) {
      for (var i = 1; i < this.percentColors.length - 1; i++) {
        if (value < this.percentColors[i].pct) break
      }
      const lower = this.percentColors[i - 1];
      const upper = this.percentColors[i];
      const range = upper.pct - lower.pct;
      const rangePct = (value - lower.pct) / range;
      const pctLower = 1 - rangePct;
      const pctUpper = rangePct;
      const color = {
          r: Math.floor(lower.color.r * pctLower + upper.color.r * pctUpper),
          g: Math.floor(lower.color.g * pctLower + upper.color.g * pctUpper),
          b: Math.floor(lower.color.b * pctLower + upper.color.b * pctUpper)
      };
      return '#' + this.componentToHex(color.g) +  this.componentToHex(color.r) +  this.componentToHex(color.b)
    },
    // Turns rgb value into hexadecimal
    componentToHex(c) {
      const hex = c.toString(16);
      return hex.length == 1 ? "0" + hex : hex;
    }
  }
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