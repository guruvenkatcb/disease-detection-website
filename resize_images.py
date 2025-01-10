import os
from PIL import Image

# Specify the input dataset directory
input_dir = "dataset"
output_dir = "resized_dataset"

# Desired image size (width, height)
image_size = (224, 224)

# Function to resize images
def resize_images(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg")):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_path)
                output_subdir = os.path.join(output_path, relative_path)

                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)

                try:
                    with Image.open(file_path) as img:
                        img_resized = img.resize(image_size)
                        output_file_path = os.path.join(output_subdir, file)
                        img_resized.save(output_file_path)
                        print(f"Resized and saved: {output_file_path}")
                except Exception as e:
                    print(f"Error resizing {file_path}: {e}")

# Resize train, test, and validation images
for folder in ["train", "test", "validation"]:
    resize_images(
        input_path=os.path.join(input_dir, folder),
        output_path=os.path.join(output_dir, folder)
    )

print("All images resized successfully!")
