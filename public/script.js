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

      // Update the status message dynamically
      status.innerHTML = `
        <p style="color: green;">${result.message}</p>
        <p><strong>Filename:</strong> ${result.filename}</p>
        <p><strong>Filepath:</strong> <a href="${result.filepath}" target="_blank">View File</a></p>
      `;
    } else {
      status.textContent = 'Error uploading file.';
    }
  } catch (err) {
    status.textContent = 'An error occurred.';
    console.error(err);
  }
});
