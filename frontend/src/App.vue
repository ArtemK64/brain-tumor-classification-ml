<template>
  <div class="app">
    <div class="container">
      <ImageUploader @prediction="updateResult" />
      <PredictionResult :result="predictionResult" />
    </div>
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
.app {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
