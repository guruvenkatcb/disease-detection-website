const express = require('express');
const multer = require('multer');
const uploadController = require('../controllers/uploadController');

const router = express.Router();

// Configure Multer
const upload = multer({ dest: 'uploads/' });

router.post('/', upload.single('file'), uploadController.uploadFile);

module.exports = router;
