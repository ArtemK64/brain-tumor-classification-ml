<template>
  <div class="image-uploader">
    <h2>Загрузите изображение МРТ</h2>
    <input type="file" @change="handleFileUpload" />
    <button @click="uploadImage">Отправить</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      file: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async uploadImage() {
      if (!this.file) {
        alert("Пожалуйста, выберите файл.");
        return;
      }

      const formData = new FormData();
      formData.append("image", this.file);

      try {
        const response = await fetch('/api/predict', {
          method: 'POST',
          body: formData,
        });
        const result = await response.json();
        this.$emit('prediction', result);
      } catch (error) {
        console.error("Ошибка загрузки изображения:", error);
      }
    },
  },
};
</script>

<style scoped>
.image-uploader {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

input[type="file"] {
  margin-bottom: 10px;
}

button {
  margin-top: 10px;
}
</style>
