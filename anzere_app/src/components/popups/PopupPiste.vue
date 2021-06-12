<template>
  <div>
    <div class="title">Piste - {{ name }}</div>
    <div class="difficulty-wrapper">
      <div 
          class="difficulty-circle"
          :style="'background-color:' + getDifficultyColor(difficulty)"/>
      <div class="difficulty-text">
        {{ getDifficultyString(difficulty) }}
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "PopupPiste",
  props: {
    name: {
      require: true,
      type: String,
    },
    difficulty: {
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
  },
  methods: {
    getDifficultyString: function(diff) {
      switch(diff) {
        case 1: return "Beginner"
        case 2: return "Intermediate"
        case 3: return "Advanced"
        case 4: return "Expert"
      }
    },
    getDifficultyColor: function(diff) {
      switch(diff) {
        case 1: return "green"
        case 2: return "blue"
        case 3: return "red"
        case 4: return "black"
      }
    }
  }
}
</script>

<style scoped>
  .title { font-size: large }
  .difficulty-text { padding-left: 0.5rem }
  .difficulty-wrapper { 
    display: flex;
    align-items: center;
  }
  .difficulty-circle {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    border: 2px solid black;
  }
</style>
