<script>
import Line from 'vue-chartjs'
export default {
  extends: Line,
  name: "Chart",
  components: {
    LineChart: Line
  },
  props: {
    data: {
      require: true,
      type: Object,
    },
    options: {
      require: false,
      type: Object,
    }
  },
  mounted () {
    this.renderChart(this.data, this.options)
  }
}
</script>

<style scoped>

</style>
