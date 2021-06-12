<template>
  <div>
    <div class="title">Restaurant - {{ name }}</div>
  </div>
</template>

<script>

export default {
  name: "PopupCommerce",
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
