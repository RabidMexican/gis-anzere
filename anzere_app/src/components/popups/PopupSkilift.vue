<template>
  <div class="popup">
    <div class="title">Skilift - {{ skilift.properties.name }}</div>
    <div class='text-wrapper'>
      <div class="capacity">Capactiy : {{ skilift.properties.capacity }} people</div>
      <div class="duration">Duration : {{ skilift.properties.duration }} minutes</div>
    </div>
    <div class="image-wrapper">
      <img src="/images/icons/skilift.png" class="icon"/>
    </div>
    <div class='chart-wrapper'>
      <LineChart :chartdata="data" :options="options" />
    </div>
  </div>
</template>


<script>
import { COLORS } from '../../constants'
import LineChart from '../charts/LineChart.vue'

export default {
  name: "PopupSkilift",
  components: {
    LineChart: LineChart
  },
  props: {
    skilift: {
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
          label: this.skilift.properties.name,
          backgroundColor: COLORS.SKILIFTS,
          data: [
            this.skilift.properties.t_0,
            this.skilift.properties.t_1,
            this.skilift.properties.t_2,
            this.skilift.properties.t_3,
            this.skilift.properties.t_4,
            this.skilift.properties.t_5,
            this.skilift.properties.t_6,
            this.skilift.properties.t_7,
            this.skilift.properties.t_8,
            this.skilift.properties.t_9,
            this.skilift.properties.t_10,
            this.skilift.properties.t_11,
            this.skilift.properties.t_12,
            this.skilift.properties.t_13,
            this.skilift.properties.t_14,
            this.skilift.properties.t_15,
            this.skilift.properties.t_16,
            this.skilift.properties.t_17,
            this.skilift.properties.t_18
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
