import tensorflow as tf  # TensorFlow library for building the model
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # To preprocess image data
from tensorflow.keras.models import Sequential  # For building the neural network model
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten  # Layers for CNN
from tensorflow.keras.optimizers import Adam  # Optimizer for training
import os  # For file system operations (optional)
