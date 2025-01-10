from flask import Flask, render_template, request, redirect, url_for  # type: ignore
import os

app = Flask(__name__)

# Existing Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detection")  # Make sure this is defined here
def detection():
    return render_template("disease_detection.html")  # Make sure this HTML exists

# New Routes
@app.route("/dataset-info")
def dataset_info():
    return render_template("dataset_info.html")  # Serves dataset_info.html

@app.route("/contact")
def contact():
    return render_template("contact.html")  # Serves contact.html

@app.route("/submit-contact", methods=["POST"])
def submit_contact():
    # Handles form submission from contact.html
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    # Save or process the contact form data
    contact_file = os.path.join("uploads", "contact_messages.txt")
    with open(contact_file, "a") as f:
        f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

    # Redirect or show a success message
    return "Thank you for contacting us! We will get back to you soon."

if __name__ == "__main__":
    app.run(debug=True)
