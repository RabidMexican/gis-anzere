import Vue from 'vue'
import App from './App.vue'
import 'leaflet/dist/leaflet.css'
import { Icon } from "leaflet"

Vue.config.productionTip = false
delete Icon.Default.prototype._getIconUrl;

// import images for Leaftlet
Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

// Create data bus
export const EventBus = new Vue()

// Add global functions
Vue.mixin({
  methods: {
    // Translate  polygon geojson coordinates 
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
    // Translate Line geojson
    getLineCoords(geojson) {
      let result = []
      geojson.forEach((top) => {
          top.forEach((bottom) => {
            bottom = new Array(bottom[1], bottom[0])
            result.push(bottom)
          })
      })
      return result
    },
    // Get color for piste difficulty
    getPisteColor (diff) { 
      switch(diff) {
        case 1: return 'green'
        case 2: return 'blue'
        case 3: return 'red'
        case 4: return 'black'
      }
    }
  }
})

// Mount the Application
new Vue({ render: h => h(App) }).$mount('#app')



