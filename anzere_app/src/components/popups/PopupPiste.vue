<template>
  <div class="popup">
    <div class="title">Piste - {{ piste.properties.name }}</div>
    <div class="difficulty-wrapper">
      <div class="difficulty-circle" :style="'background-color:' + getPisteColor(piste.properties.difficulty)"/>
      <div class="difficulty-text">{{ getDifficultyString() }}</div>
    </div>
    <div class="chart-wrapper">
      <LineChart :chartdata="data" :options="options"/>
    </div>
  </div>
  
</template>

<script>
import LineChart from '../charts/LineChart.vue'
export default {
  name: "PopupPiste",
  components: {
    LineChart: LineChart,
  },
  props: {
    piste: {
      require: true,
      type: Object,
    },
  },
  data() {
    return {
      options: {
        legend: {
          display: false
        },
        title: {
            display: true,
            text: 'Traffic by hour (% of total)',
        },
        scales: {
          yAxes : [{
              ticks : {
                  max : 30,
              }
          }]
        }
      }
    }
  },
  methods: {
    // Get name of piste difficulty
    getDifficultyString: function() {
      switch(this.piste.properties.difficulty) {
        case 1: return "Beginner"
        case 2: return "Intermediate"
        case 3: return "Advanced"
        case 4: return "Expert"
      }
    },
  },
    computed: {
    data() {
      return {
        labels: ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00',  '12:30', '13:00', '13:30', '14:00', '14:30', '15:00:', '15:30', '16:00', '16:30', '17:00'],
        datasets: [{
          label: this.piste.properties.name,
          backgroundColor: this.getPisteColor(this.piste.properties.difficulty),
          data: [
            this.piste.properties.t_0,
            this.piste.properties.t_1,
            this.piste.properties.t_2,
            this.piste.properties.t_3,
            this.piste.properties.t_4,
            this.piste.properties.t_5,
            this.piste.properties.t_6,
            this.piste.properties.t_7,
            this.piste.properties.t_8,
            this.piste.properties.t_9,
            this.piste.properties.t_10,
            this.piste.properties.t_11,
            this.piste.properties.t_12,
            this.piste.properties.t_13,
            this.piste.properties.t_14,
            this.piste.properties.t_15,
            this.piste.properties.t_16,
            this.piste.properties.t_17,
            this.piste.properties.t_18
          ]
        }]
      }
    },
  }
}
</script>

<style scoped>
  .popup { min-width: 300px }
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
