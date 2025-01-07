const path = require('path');

exports.uploadFile = (req, res) => {
  if (!req.file) {
    return res.status(400).send({ error: 'No file uploaded!' });
  }

  res.send({
    message: 'File uploaded successfully!',
    filename: req.file.originalname,
    filepath: req.file.path,
  });
};
