<template>
  <div>
    <div class="title">{{ name }}</div>
    <i>{{ getType(type) }}</i>
    <div>Number of places : {{ places }}</div>
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
    type: {
      require: true,
      type: Number,
    },
    places: {
      require: true,
      type: Number,
    }
  },
  methods: {
    getType: function(type) {
      switch(type) {
        case 1: return "Restaurant"
        case 2: return "Bar"
      }
    }
  }
}
</script>

<style scoped>
  .title { font-size: large }
</style>
