<template>
  <div>
    <div class="title">Telecabine - {{ telecabine.properties.name }}</div>
    <div class="capacity">Capactiy : {{ telecabine.properties.capacity }} people</div>
    <div class="duration">Duration : {{ telecabine.properties.duration }} minutes</div>
    <div class="image-wrapper">
      <img src="/images/icons/telecabine.png" class="icon"/>
    </div>
  </div>
</template>

<script>

export default {
  name: "PopupTelecabine",
  props: {
    telecabine: {
      require: true,
      type: Object,
    },
  },
}
</script>

<style scoped>
  .title { 
    font-size: large;
    margin-bottom: 1rem;
  }
  .icon {
    width: 8rem;
    right: 0; 
  }
  .image-wrapper {
    text-align: right;
  }
</style>
