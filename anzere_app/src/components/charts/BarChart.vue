<script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,
  name: 'LineChart',
  props: ['chartdata', 'options'],
  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>

<style>
</style>