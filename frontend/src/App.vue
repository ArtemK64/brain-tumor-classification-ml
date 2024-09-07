<template>
  <div class="app">
    <ImageUploader @prediction="updateResult" />
    <PredictionResult :result="predictionResult" />
  </div>
</template>

<script>
import ImageUploader from '@/components/ImageUploader.vue';
import PredictionResult from '@/components/PredictionResult.vue';

export default {
  components: {
    ImageUploader,
    PredictionResult,
  },
  data() {
    return {
      predictionResult: null,
    };
  },
  methods: {
    updateResult(result) {
      this.predictionResult = result;
    },
  },
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
