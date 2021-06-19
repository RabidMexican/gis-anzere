<template>
  <div class="popup">
    <div class="title">Station - {{ station.properties.name }}</div>
    <div class='chart-wrapper'>
      <LineChart :chartdata="data" :options="options" />
    </div>
  </div>
</template>


<script>
import { COLORS } from '../../constants'
import LineChart from '../charts/LineChart.vue'
export default {
  name: "PopupStation",
  components: {
    LineChart: LineChart
  },
  props: {
    station: {
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
          label: this.station.properties.name,
          backgroundColor: COLORS.STATIONS,
          data: [
            this.station.properties.t_0,
            this.station.properties.t_1,
            this.station.properties.t_2,
            this.station.properties.t_3,
            this.station.properties.t_4,
            this.station.properties.t_5,
            this.station.properties.t_6,
            this.station.properties.t_7,
            this.station.properties.t_8,
            this.station.properties.t_9,
            this.station.properties.t_10,
            this.station.properties.t_11,
            this.station.properties.t_12,
            this.station.properties.t_13,
            this.station.properties.t_14,
            this.station.properties.t_15,
            this.station.properties.t_16,
            this.station.properties.t_17,
            this.station.properties.t_18
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
    margin-bottom: 1rem;
  }
  .icon {
    width: 5rem;
    right: 0; 
  }
  .image-wrapper {
    text-align: right;
  }
  .popup {
    min-width: 300px;
  }
</style>
