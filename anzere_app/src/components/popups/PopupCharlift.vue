<template>
 <div>
    <div class="title">Charlift - {{ charlift.properties.name }}</div>
    <div class="capacity">Capactiy : {{ charlift.properties.capacity }} people</div>
    <div class="duration">Duration : {{ charlift.properties.duration }} minutes</div>
    <div class="image-wrapper">
      <img src="/images/icons/charlift.png" class="icon"/>
    </div>
  </div>
</template>

<script>

export default {
  name: "PopupChairlift",
  props: {
    charlift: {
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
