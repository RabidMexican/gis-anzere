<template>
  <div class="popup">
    <div class="title">{{ parking.properties.name }}</div>
    <div v-bind:class="parking.properties.free ? 'free' : 'paid'" class="price">
      {{ priceText }}
    </div>
    <div class="icon-wrapper">
      <div class="capacity">Capacity : {{ parking.properties.nb_place }} places</div>
      <img src="/images/icons/parking.png" class="icon">
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
  name: "PopupParking",
  components: {
    LineChart: LineChart,
  },
  props: {
    parking: {
      require: true,
      type: Object,
    },
  },
  data() {
    return {
      priceText: 'Free',
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
  mounted() {
    if(!this.parking.properties.free) this.priceText = 'Pay to stay'
  },
  computed: {
    data() {
      return {
        labels: ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00',  '12:30', '13:00', '13:30', '14:00', '14:30', '15:00:', '15:30', '16:00', '16:30', '17:00'],
        datasets: [{
          label: this.parking.properties.name,
          backgroundColor: COLORS.PARKING,
          data: [
            this.parking.properties.t_0,
            this.parking.properties.t_1,
            this.parking.properties.t_2,
            this.parking.properties.t_3,
            this.parking.properties.t_4,
            this.parking.properties.t_5,
            this.parking.properties.t_6,
            this.parking.properties.t_7,
            this.parking.properties.t_8,
            this.parking.properties.t_9,
            this.parking.properties.t_10,
            this.parking.properties.t_11,
            this.parking.properties.t_12,
            this.parking.properties.t_13,
            this.parking.properties.t_14,
            this.parking.properties.t_15,
            this.parking.properties.t_16,
            this.parking.properties.t_17,
            this.parking.properties.t_18
          ]
        }]
      }
    },
  }
}
</script>

<style scoped>
  .popup { 
    min-width: 300px 
  }
  .title { font-size: large }
  .price { font-size: large }
  .capacity { 
    margin-top: 5px;
    margin-right: 10px;
  }
  .free { color: green }
  .paid { color: red }
  .icon-wrapper { 
    display: flex; 
    justify-content: space-between;
  }
  .icon {
    width: 50px;
    height: 50px;
  }
</style>
