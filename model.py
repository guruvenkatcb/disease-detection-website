import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define image size (224x224 for CNNs)
img_size = (224, 224)

# Set up ImageDataGenerator for preprocessing and augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,               # Normalize the pixel values to [0, 1]
    rotation_range=20,            # Randomly rotate images
    width_shift_range=0.2,        # Randomly shift images horizontally
    height_shift_range=0.2,       # Randomly shift images vertically
    shear_range=0.2,              # Randomly shear images
    zoom_range=0.2,               # Randomly zoom in/out images
    horizontal_flip=True,         # Randomly flip images horizontally
    fill_mode='nearest'           # Fill in missing pixels
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Define directories for your dataset
train_dir = 'dataset/train'
test_dir = 'dataset/test'

# Load train and test datasets
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=img_size,
    batch_size=32,
    class_mode='binary'  # Use 'binary' for two classes (healthy vs disease)
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    batch_size=32,
    class_mode='binary'
)

# Build the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,  # Adjust epochs as needed
    validation_data=test_generator,
    validation_steps=test_generator.samples // test_generator.batch_size
)

# Save the trained model as model.h5
model.save('model.h5')
