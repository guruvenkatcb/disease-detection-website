const express = require('express');
const analysisController = require('../controllers/analysisController');

const router = express.Router();

router.post('/', analysisController.analyzeDocument);

module.exports = router;
