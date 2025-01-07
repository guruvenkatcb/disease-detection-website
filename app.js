const express = require('express');
const cors = require('cors');
const path = require('path');

// Import Routes
const uploadRoutes = require('./routes/upload');
const analysisRoutes = require('./routes/analysis');

const app = express();
const PORT = 5000;

// Middleware
app.use(cors());
app.use(express.json());

// Serve Frontend
app.use(express.static(path.join(__dirname, 'disease-detection-website')));

// API Routes
app.use('/api/upload', uploadRoutes);
app.use('/api/analysis', analysisRoutes);

// Default Route for Frontend
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'disease-detection-website', 'index.html'));
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
