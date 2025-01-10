import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, save_img
import numpy as np

# Paths to dataset folders
dataset_dir = os.path.join(os.getcwd(), 'dataset')
train_dir = os.path.join(dataset_dir, 'train')

# Folder names for the classes
healthy_folder = os.path.join(train_dir, 'healthy')
pneumonia_folder = os.path.join(train_dir, 'pneumonia')

# Folder to save augmented images
augmented_dir = os.path.join(dataset_dir, 'augmented')
os.makedirs(augmented_dir, exist_ok=True)

augmented_healthy = os.path.join(augmented_dir, 'healthy')
augmented_pneumonia = os.path.join(augmented_dir, 'pneumonia')

os.makedirs(augmented_healthy, exist_ok=True)
os.makedirs(augmented_pneumonia, exist_ok=True)

# Data augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

def augment_images(input_folder, output_folder, target_count):
    """
    Augments images in the input folder to reach the target count in the output folder.
    """
    # Get all images in the folder
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    print(f"Found {len(image_files)} images in {input_folder}")

    current_count = len(image_files)
    images_to_generate = target_count - current_count
    print(f"Generating {images_to_generate} additional images for {input_folder}")

    if images_to_generate <= 0:
        print(f"No augmentation needed for {input_folder}")
        return

    counter = 0
    for img_file in image_files:
        img_path = os.path.join(input_folder, img_file)
        img = load_img(img_path)  # Load image
        img_array = img_to_array(img)  # Convert to numpy array
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Generate augmented images
        for batch in datagen.flow(img_array, batch_size=1, save_to_dir=output_folder, save_prefix='aug', save_format='jpeg'):
            counter += 1
            if counter >= images_to_generate:
                print(f"Augmentation complete for {input_folder}")
                return

# Count images in each folder
healthy_count = len(os.listdir(healthy_folder))
pneumonia_count = len(os.listdir(pneumonia_folder))

# Determine the target count for each class
target_count = max(healthy_count, pneumonia_count)

# Augment images in each class
augment_images(healthy_folder, augmented_healthy, target_count)
augment_images(pneumonia_folder, augmented_pneumonia, target_count)

print("Augmentation process completed!")
