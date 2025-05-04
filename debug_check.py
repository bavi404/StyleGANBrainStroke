import os

print("Checking stroke folder:")
print("Exists:", os.path.exists("data/real_mri/stroke"))
if os.path.exists("data/real_mri/stroke"):
    print("Contents:", os.listdir("data/real_mri/stroke"))

print("\nChecking no_stroke folder:")
print("Exists:", os.path.exists("data/real_mri/no_stroke"))
if os.path.exists("data/real_mri/no_stroke"):
    print("Contents:", os.listdir("data/real_mri/no_stroke"))
