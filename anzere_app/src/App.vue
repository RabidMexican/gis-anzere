<template>
  <div id="app">
    <ControlPanel/>
    <Map/>
  </div>
</template>

<script>
import Map from './components/AnzereMap.vue'
import ControlPanel from './components/ControlPanel.vue'

export default {
  name: 'App',
  components: {
    Map,
    ControlPanel,
  }
}
</script>

<style>
  body {
    margin: 0;
    font-family: 'Open Sans', sans-serif;
  }
</style>
