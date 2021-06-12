<template>
  <div>
    <div class="title">Ski Lift - {{ name }}</div>
  </div>
</template>

<script>

export default {
  name: "PopupSkilift",
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
