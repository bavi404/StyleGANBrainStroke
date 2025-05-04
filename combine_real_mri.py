import os
import shutil

# Define source and output
stroke_dir = "data/real_mri/stroke"
no_stroke_dir = "data/real_mri/no_stroke"
output_dir = "data/real_mri_combined"

# Create the output folder
os.makedirs(output_dir, exist_ok=True)

def copy_images(src_folder, label):
    images = sorted([f for f in os.listdir(src_folder) if f.endswith(".png")])
    for i, filename in enumerate(images):
        src = os.path.join(src_folder, filename)
        dst_filename = f"{label}_{i+1:03d}.png"
        dst = os.path.join(output_dir, dst_filename)
        shutil.copy(src, dst)
        print(f"✅ Copied {filename} → {dst_filename}")

# Copy stroke and no_stroke images
print("📦 Combining real MRI images...")
copy_images(stroke_dir, "stroke")
copy_images(no_stroke_dir, "no_stroke")

print(f"\n🎉 Done! Combined images saved to: {output_dir}")
