from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Disease Detection route
@app.route("/detection")
def detection():
    return render_template("disease_detection.html")

# Dataset Info route
@app.route("/dataset-info")
def dataset_info():
    return render_template("dataset_info.html")

# Contact Us route
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Contact form submission handler
@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Save contact message to file (or you could store in database)
    contact_file = os.path.join("uploads", "contact_messages.txt")
    with open(contact_file, "a") as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

    return "Thank you for contacting us! We will get back to you soon."

if __name__ == "__main__":
    app.run(debug=True)
