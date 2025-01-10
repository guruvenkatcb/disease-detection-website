from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# Set up a folder to store uploaded files (if it doesn't exist)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Load the pre-trained model (make sure model.h5 exists in the directory)
model = tf.keras.models.load_model('model.h5')

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to serve the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route to serve the disease detection page
@app.route("/detection")
def detection():
    return render_template("disease_detection.html")

# Route to process the contact form
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Route to handle file upload and disease detection
@app.route("/detect", methods=["POST"])
def detect_disease():
    if 'image' not in request.files:
        return "No file part"
    
    file = request.files['image']
    
    if file.filename == '':
        return "No selected file"
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Preprocess the image for prediction
        img = image.load_img(filepath, target_size=(224, 224))  # Resize based on model input size
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Normalize image (if needed by your model)
        img_array = img_array / 255.0

        # Get prediction from the model
        prediction = model.predict(img_array)

        # Assuming your model outputs a probability for each class, for example:
        # 0 = Healthy, 1 = Pneumonia
        if prediction[0][0] > 0.5:
            result = "Pneumonia Detected"
        else:
            result = "Healthy"

        return render_template("detection_result.html", result=result, image_path=filepath)
    else:
        return "Invalid file format"

# Route to display the result (disease detection outcome)
@app.route("/result")
def result():
    return render_template("detection_result.html", result="No result yet")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
