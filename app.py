import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Load your trained model
model = load_model('model.h5')  # Path to your trained model file

# Set up the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check allowed extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the homepage (upload form)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess the image and make prediction
        img = image.load_img(filepath, target_size=(224, 224))  # Adjust size as per your model
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Normalization if needed
        img_array = img_array / 255.0

        # Predict the class
        prediction = model.predict(img_array)
        
        # Assuming your model outputs probabilities, you might need to adjust based on the model output
        if prediction[0][0] > 0.5:
            result = "Disease"
        else:
            result = "Healthy"
        
        return jsonify({'prediction': result})

    else:
        return jsonify({'error': 'Invalid file type'})

if __name__ == '__main__':
    app.run(debug=True)
