from PIL import Image
import os

input_folder = "data/real_mri_combined"
output_folder = "data/real_mri_rgb_256"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        img = Image.open(os.path.join(input_folder, filename)).convert("RGB")
        img = img.resize((256, 256))
        img.save(os.path.join(output_folder, filename))

print("✅ Preprocessing complete.")
