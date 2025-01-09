document.getElementById('analyzeButton').addEventListener('click', async () => {
  const fileInput = document.getElementById('imageUpload');
  const file = fileInput.files[0];
  
  if (!file) {
      alert("Please upload an image.");
      return;
  }

  const formData = new FormData();
  formData.append('image', file);

  try {
      const response = await fetch('/analyze', { method: 'POST', body: formData });
      const result = await response.json();
      document.getElementById('resultSection').style.display = 'block';
      document.getElementById('resultText').textContent = `Result: ${result.prediction}`;
  } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while analyzing the image.");
  }
});
