from flask import Flask, request, jsonify
from tensorflow import keras
import numpy as np
import io
from PIL import Image

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = keras.models.load_model('models/brain_tumor_classifier.keras')

CATEGORIES = ['Без опухоли', 'Опухоль гипофиза', 'Менингиома', 'Глиома']

def predict_image(img):
    img = Image.open(img).convert('RGB')
    img = img.resize((150, 150))
    img_array = np.array(img).astype('float32')
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    prediction = model.predict(img_array)
    return prediction

@app.route('/api/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400

    file = request.files['image']
    img = io.BytesIO(file.read())

    try:
        prediction = predict_image(img)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    predicted_category_index = np.argmax(prediction)
    predicted_category = CATEGORIES[predicted_category_index]
    confidence = float(prediction[0][predicted_category_index]) * 100

    response = {
        'prediction': predicted_category,
        'confidence': confidence
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
