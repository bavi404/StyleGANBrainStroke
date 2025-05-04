import subprocess
import os

stylegan_dir = "stylegan2-ada-pytorch"
dataset_tool = os.path.join(stylegan_dir, "dataset_tool.py")

subprocess.run([
    "python", dataset_tool,
    "--source=data/real_mri_rgb_256",
    "--dest=data/real_mri_256.zip"
])
