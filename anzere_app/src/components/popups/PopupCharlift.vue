<template>
  <div>
    <div class="title">Chairlift - {{ name }}</div>
  </div>
</template>

<script>

export default {
  name: "PopupChairlift",
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
