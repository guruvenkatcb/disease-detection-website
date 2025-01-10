// static/js/preview.js

function previewImage(event) {
    const file = event.target.files[0];  // Get the selected file
    const reader = new FileReader();  // Create a new FileReader instance

    reader.onload = function() {
        const preview = document.getElementById("preview");  // Get the preview image element
        preview.src = reader.result;  // Set the source to the file's data URL
        preview.style.display = "block";  // Display the image element
    }

    if (file) {
        reader.readAsDataURL(file);  // Read the file as a data URL
    }
}
