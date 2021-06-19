<template>
  <div class="popup">
    <div class="title">{{ shop.properties.name }}</div>
    <i>{{ getType() }}</i>
    <div>Number of places : {{ shop.properties.nb_place }}</div>
    <div class="chart-wrapper">
      <LineChart :chartdata="data" :options="options" />
    </div>
  </div>
</template>

<script>
import LineChart from '../charts/LineChart.vue'
import { COLORS } from '../../constants'
export default {
  name: "PopupCommerce",
  components: {
    LineChart: LineChart,
  },
  props: {
    shop: {
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
    getType() {
      switch(this.shop.properties.type) {
        case 1: return "Restaurant"
        case 2: return "Bar"
      }
    }
  },
  computed: {
    data() {
      return {
        labels: ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00',  '12:30', '13:00', '13:30', '14:00', '14:30', '15:00:', '15:30', '16:00', '16:30', '17:00'],
        datasets: [{
          label: this.shop.properties.name,
          backgroundColor: COLORS.COMMERCE,
          data: [
            this.shop.properties.t_0,
            this.shop.properties.t_1,
            this.shop.properties.t_2,
            this.shop.properties.t_3,
            this.shop.properties.t_4,
            this.shop.properties.t_5,
            this.shop.properties.t_6,
            this.shop.properties.t_7,
            this.shop.properties.t_8,
            this.shop.properties.t_9,
            this.shop.properties.t_10,
            this.shop.properties.t_11,
            this.shop.properties.t_12,
            this.shop.properties.t_13,
            this.shop.properties.t_14,
            this.shop.properties.t_15,
            this.shop.properties.t_16,
            this.shop.properties.t_17,
            this.shop.properties.t_18
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
</style>
