import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
data_dir = "resized_dataset/disease"
train_dir = "resized_dataset/train"
test_dir = "resized_dataset/test"
val_dir = "resized_dataset/validation"

# Create directories
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# List all images
images = os.listdir(data_dir)

# Split into train, test, and validation
train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
train_images, val_images = train_test_split(train_images, test_size=0.25, random_state=42)  # 0.25 x 0.8 = 0.2

# Move images to respective folders
for img in train_images:
    shutil.copy(os.path.join(data_dir, img), train_dir)

for img in test_images:
    shutil.copy(os.path.join(data_dir, img), test_dir)

for img in val_images:
    shutil.copy(os.path.join(data_dir, img), val_dir)
