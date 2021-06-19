<template>
 <div class="popup">
    <div class="title">Chairlift - {{ chairlift.properties.name }}</div>
    <div class="capacity">Capactiy : {{ chairlift.properties.capacity }} people</div>
    <div class="duration">Duration : {{ chairlift.properties.duration }} minutes</div>
    <div class="image-wrapper">
      <img src="/images/icons/chairlift.png" class="icon"/>
    </div>
    <div class="chart-wrapper">
      <LineChart :chartdata="data" :options="options" />
    </div>
  </div>
</template>

<script>
import LineChart from '../charts/LineChart.vue'
import { COLORS } from '../../constants'
export default {
  name: "PopupChairlift",
  components: {
    LineChart: LineChart,
  },
  props: {
    chairlift: {
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
  computed: {
    data() {
      return {
        labels: ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00',  '12:30', '13:00', '13:30', '14:00', '14:30', '15:00:', '15:30', '16:00', '16:30', '17:00'],
        datasets: [{
          label: this.chairlift.properties.name,
          backgroundColor: COLORS.CHAIRLIFTS,
          data: [
            this.chairlift.properties.t_0,
            this.chairlift.properties.t_1,
            this.chairlift.properties.t_2,
            this.chairlift.properties.t_3,
            this.chairlift.properties.t_4,
            this.chairlift.properties.t_5,
            this.chairlift.properties.t_6,
            this.chairlift.properties.t_7,
            this.chairlift.properties.t_8,
            this.chairlift.properties.t_9,
            this.chairlift.properties.t_10,
            this.chairlift.properties.t_11,
            this.chairlift.properties.t_12,
            this.chairlift.properties.t_13,
            this.chairlift.properties.t_14,
            this.chairlift.properties.t_15,
            this.chairlift.properties.t_16,
            this.chairlift.properties.t_17,
            this.chairlift.properties.t_18
          ]
        }]
      }
    },
  }
}
</script>

<style scoped>
  .popup { min-width: 300px }
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
