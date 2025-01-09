from flask import Flask, request, jsonify, render_template
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Folder for uploads
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the trained model
model = load_model('model.h5')

# Route for home
@app.route('/')
def index():
    return render_template('index.html')  # Ensure index.html is in the templates folder

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(img_path)

    # Preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Make a prediction
    prediction = model.predict(img_array)
    result = 'Disease' if prediction[0][0] > 0.5 else 'Healthy'

    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
