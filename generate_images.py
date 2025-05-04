import subprocess

subprocess.run([
    "python", "generate.py",
    "--outdir=data/generated",
    "--trunc=0.7",
    "--seeds=0-99",
    "--network=training-runs/YOUR_RUN_FOLDER/network-snapshot-XXXX.pkl"
])
