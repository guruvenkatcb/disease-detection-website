document.getElementById('uploadForm').addEventListener('submit', function (e) {
    alert('File uploaded successfully!');
});
document.getElementById('uploadForm').addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent form submission
  
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    const status = document.getElementById('status');
  
    if (!file) {
      status.textContent = 'No file selected!';
      return;
    }
  
    const formData = new FormData();
    formData.append('file', file);
  
    try {
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
  
      if (response.ok) {
        const result = await response.json();
        status.textContent = `Uploaded: ${result.filename}`;
      } else {
        status.textContent = 'Error uploading file.';
      }
    } catch (err) {
      status.textContent = 'An error occurred.';
      console.error(err);
    }
  });
  