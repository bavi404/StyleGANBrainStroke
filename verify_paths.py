import os

print("📍 Current Working Directory:", os.getcwd())

print("\n🔎 Folders:")
print("Stroke Folder Exists:", os.path.exists("data/real_mri/stroke"))
print("No Stroke Folder Exists:", os.path.exists("data/real_mri/no_stroke"))

print("\n📂 Output Folder Will Be:")
print("data/real_mri_combined")

print("\n📷 Stroke Images:")
print(os.listdir("data/real_mri/stroke"))

print("\n📷 No-Stroke Images:")
print(os.listdir("data/real_mri/no_stroke"))
