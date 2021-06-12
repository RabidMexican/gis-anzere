<template>
  <div>
    <div class="title">{{ name }}</div>
    <div v-bind:class="free ? 'free' : 'paid'" class="price">
      {{ priceText }}
    </div>
    <div class="capacity">Capacity : {{ capacity }}</div>
  </div>
</template>

<script>

export default {
  name: "PopupParking",
  props: {
    name: {
      require: true,
      type: String,
    },
    capacity: {
      require: true,
      type: Number,
    },
    free: {
      require: true,
      type: Boolean,
    }
  },
  data() {
    return {
      priceText: 'Free'
    }
  },
  mounted() {
    if(!this.free)
      this.priceText = 'Pay to stay'
  }
}
</script>

<style scoped>
  .title { font-size: large }
  .price { font-size: large }
  .capacity { margin-top: 5px }
  .free { color: green }
  .paid { color: red }
</style>
