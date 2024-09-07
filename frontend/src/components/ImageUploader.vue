<template>
  <div class="image-uploader">
    <h2>Загрузите изображение МРТ</h2>
    <input type="file" @change="handleFileUpload" />
    <button @click="uploadImage" :disabled="!file">Отправить</button>
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
      const file = event.target.files[0];
      const allowedTypes = ['image/jpeg', 'image/png', 'image/bmp', 'image/gif', 'image/tiff'];

      if (file && allowedTypes.includes(file.type)) {
        this.file = file;
      } else {
        alert('Неподдерживаемый формат файла. Пожалуйста, загрузите изображение в формате JPEG, PNG, BMP, GIF или TIFF.');
        this.file = null;
      }
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
  justify-content: center;
  padding: 20px;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 700px;
  margin: 20px;
}

input[type="file"] {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
