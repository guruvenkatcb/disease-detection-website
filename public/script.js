// Attach an event listener to the form submission
document.getElementById('uploadForm').addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent the form from submitting in the usual way

  const fileInput = document.getElementById('fileInput'); // Get the file input
  const file = fileInput.files[0]; // Get the selected file
  const status = document.getElementById('status'); // Get the status paragraph

  // Check if no file is selected
  if (!file) {
      status.textContent = 'No file selected!'; // Show error message if no file is selected
      return; // Exit the function
  }

  const formData = new FormData(); // Create a new FormData object to send the file
  formData.append('file', file); // Append the selected file to the FormData object

  try {
      // Send the file to the backend using the fetch function
      const response = await fetch('/upload', { // Make sure this matches the route in your backend
          method: 'POST',
          body: formData, // Send the file in the request body
      });

      // If the upload was successful
      if (response.ok) {
          const result = await response.json(); // Get the server's response
          status.textContent = `Uploaded: ${result.filename}`; // Show the uploaded filename
          alert('File uploaded successfully!'); // Show the success alert
      } else {
          status.textContent = 'Error uploading file.'; // Show error message if something went wrong
      }
  } catch (err) {
      status.textContent = 'An error occurred.'; // Handle errors and show error message
      console.error(err); // Log the error to the console for debugging
  }
});
