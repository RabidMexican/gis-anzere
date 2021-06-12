<template>
  <div>
    <div class="title">Station - {{ name }}</div>
  </div>
</template>

<script>

export default {
  name: "PopupStation",
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
