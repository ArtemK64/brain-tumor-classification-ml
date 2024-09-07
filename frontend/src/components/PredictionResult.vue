<template>
  <div class="prediction-result">
    <h2>Результат классификации</h2>
    <p v-if="result">
      <strong>Прогноз:</strong> {{ result.prediction }}<br>
      <strong>Точность:</strong> {{ result.confidence.toFixed(2) }}%
    </p>
    <p v-else>Загрузите изображение, чтобы увидеть результат.</p>
  </div>
</template>

<script>
export default {
  props: {
    result: Object,
  },
};
</script>

<style scoped>
.prediction-result {
  text-align: center;
  margin-top: 20px;
  padding: 20px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 700px;
  margin: 20px auto; /* Центрируем блок на странице */
}
</style>
