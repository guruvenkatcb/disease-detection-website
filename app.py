from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
import os

# Initialize the Flask app
app = Flask(__name__, static_folder='public')  # static folder for public assets

# Load the trained model (ensure model.h5 exists in your folder)
model = load_model('model.h5')

# Route for the homepage, showing the main form for uploading images
@app.route('/')
def home():
    return render_template('index.html')  # Render the homepage

# Route for predicting the disease (for uploaded images)
@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image file from the form
    file = request.files['image']  # Access the file from the form submission
    
    # Open the image file
    img = Image.open(io.BytesIO(file.read()))  # Convert file to Image object
    
    # Preprocess the image (resize and normalize it)
    img = img.resize((150, 150))  # Resize image to 150x150 pixels (model's input size)
    img_array = np.array(img) / 255.0  # Normalize pixel values (between 0 and 1)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension (necessary for prediction)
    
    # Make the prediction using the loaded model
    prediction = model.predict(img_array)
    
    # Return prediction as JSON response
    return jsonify({'prediction': prediction[0][0]})  # Output prediction as JSON

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
