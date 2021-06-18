<template>
 <div>
    <div class="title">Skilift - {{ skilift.properties.name }}</div>
    <div class="capacity">Capactiy : {{ skilift.properties.capacity }} people</div>
    <div class="duration">Duration : {{ skilift.properties.duration }} minutes</div>
    <div class="image-wrapper">
      <img src="/images/icons/skilift.png" class="icon"/>
    </div>
  </div>
</template>

<script>

export default {
  name: "PopupSkilift",
  props: {
    skilift: {
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
    width: 5rem;
    right: 0; 
  }
  .image-wrapper {
    text-align: right;
  }
</style>
