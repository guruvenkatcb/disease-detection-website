from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import os

# Initialize the Flask app with custom static folder
app = Flask(__name__, static_folder='public')

# Load the trained model (ensure model.h5 exists)
model = load_model('model.h5')

# Home route to display the main webpage
@app.route('/')
def home():
    return render_template('index.html')

# Predict route to handle file uploads and make predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image file from the form
    file = request.files['image']
    img = Image.open(io.BytesIO(file.read()))  # Open image from uploaded file
    
    # Preprocess image (resize, normalize, etc.)
    img = img.resize((150, 150))
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Make prediction using the loaded model
    prediction = model.predict(img_array)
    
    # Return prediction as a response
    return jsonify({'prediction': prediction[0][0]})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
