<template>
  <div class="control-panel">
    <img id="logo" src="/images/anzere.png"/>
    <div style="height:500px"></div>
  </div>
</template>

<script>

export default {
  name: "ControlPanel"
}
</script>

<style scoped>
#logo { width: 20rem }
.control-panel {
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
</style>
