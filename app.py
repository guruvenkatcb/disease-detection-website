from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set up a folder to store uploaded files (if it doesn't exist)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

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
        
        # Here you would add the logic to process the image and perform disease detection
        # For now, we'll simulate the result
        # Example: result = detect_disease_in_image(filepath)
        result = "Pneumonia Detected"  # This is a placeholder for your actual detection logic

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
