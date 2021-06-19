<template>
  <div>
    <div class="title">Telecabine - {{ telecabine.properties.name }}</div>
    <div class='text-wrapper'>
      <div class="capacity">Capactiy : {{ telecabine.properties.capacity }} people</div>
      <div class="duration">Duration : {{ telecabine.properties.duration }} minutes</div>
    </div>
    <div class="image-wrapper">
      <img src="/images/icons/telecabine.png" class="icon"/>
    </div>
    <div class='chart-wrapper'>
      <LineChart :chartdata="data" :options="options" />
    </div>
  </div>
</template>

<script>
import LineChart from '../charts/LineChart.vue'
import { COLORS } from '../../constants'
export default {
  name: "PopupTelecabine",
  components: {
    LineChart: LineChart,
  },
  props: {
    telecabine: {
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
          label: this.telecabine.properties.name,
          backgroundColor: COLORS.TELECABINES,
          data: [
            this.telecabine.properties.t_0,
            this.telecabine.properties.t_1,
            this.telecabine.properties.t_2,
            this.telecabine.properties.t_3,
            this.telecabine.properties.t_4,
            this.telecabine.properties.t_5,
            this.telecabine.properties.t_6,
            this.telecabine.properties.t_7,
            this.telecabine.properties.t_8,
            this.telecabine.properties.t_9,
            this.telecabine.properties.t_10,
            this.telecabine.properties.t_11,
            this.telecabine.properties.t_12,
            this.telecabine.properties.t_13,
            this.telecabine.properties.t_14,
            this.telecabine.properties.t_15,
            this.telecabine.properties.t_16,
            this.telecabine.properties.t_17,
            this.telecabine.properties.t_18
          ]
        }]
      }
    },
  }
}
</script>

<style scoped>
  .title { 
    font-size: large;
    margin-bottom: 0.8rem;
  }
  .icon {
    width: 4rem;
    right: 0; 
  }
  .chart-wrapper {
    text-align: center;
  }
  .image-wrapper {
    text-align: right;
    display: inline-block;
    width: 50%;
    vertical-align:top
  }
  .text-wrapper {
    display: inline-block;
    vertical-align:top
  }
</style>
