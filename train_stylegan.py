import subprocess
import os

stylegan_dir = "stylegan2-ada-pytorch"  # or full path if needed
train_script = os.path.join(stylegan_dir, "train.py")

subprocess.run([
    "python", train_script,
    "--outdir=training-runs",
    "--data=data/real_mri_256.zip",
    "--gpus=1",
    "--cfg=auto",
    "--aug=ada"
])
