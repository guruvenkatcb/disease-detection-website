document.getElementById('uploadForm').addEventListener('submit', async (event) => {
  event.preventDefault(); // Prevent default form submission

  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];
  const status = document.getElementById('status');

  // Check if a file is selected
  if (!file) {
      status.textContent = 'No file selected!';
      return;
  }

  const formData = new FormData();
  formData.append('file', file);

  try {
      // Make the fetch request to the backend
      const response = await fetch('/upload', { // Adjusted URL if your backend route is `/upload`
          method: 'POST',
          body: formData,
      });

      // Handle the response
      if (response.ok) {
          const result = await response.json();
          status.textContent = `Uploaded: ${result.filename}`;
          alert('File uploaded successfully!'); // Alert after successful upload
      } else {
          status.textContent = 'Error uploading file.';
      }
  } catch (err) {
      status.textContent = 'An error occurred.';
      console.error(err);
  }
});
