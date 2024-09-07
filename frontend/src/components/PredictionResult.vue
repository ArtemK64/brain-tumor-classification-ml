<template>
  <div class="prediction-result">
    <h2>Результат классификации</h2>
    <p v-if="result">{{ result }}</p>
    <p v-else>Загрузите изображение, чтобы увидеть результат.</p>
  </div>
</template>

<script>
export default {
  props: {
    result: String,
  },
};
</script>

<style scoped>
.prediction-result {
  text-align: center;
  margin-top: 20px;
}
</style>
