<template>
  <div>
    <div class="title">Telecabine - {{ name }}</div>
  </div>
</template>

<script>

export default {
  name: "PopupTelecabine",
  props: {
    name: {
      require: true,
      type: String,
    },
  },
}
</script>

<style scoped>
  .title { font-size: large }
</style>
