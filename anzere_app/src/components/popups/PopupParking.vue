<template>
  <div id="popup">
    <div class="title">{{ name }}</div>
    <div v-bind:class="free ? 'free' : 'paid'" class="price">
      {{ priceText }}
    </div>
    <div class="icon-wrapper">
      <div class="capacity">Capacity : {{ capacity }}</div>
      <img src="/images/icons/parking.png" class="icon">
    </div>
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
      type: Number,
    }
  },
  data() {
    return {
      priceText: 'Free'
    }
  },
  mounted() {
    if(!this.free) this.priceText = 'Pay to stay'
  }
}
</script>

<style scoped>
  .title { font-size: large }
  .price { font-size: large }
  .capacity { 
    margin-top: 5px;
    margin-right: 10px;
  }
  .free { color: green }
  .paid { color: red }
  .icon-wrapper { 
    display: flex; 
    justify-content: space-between;
  }
  .icon {
    width: 50px;
    height: 50px;
  }
</style>
