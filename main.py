import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app_path = os.path.join(BASE_DIR, "dashboard", "app.py")

subprocess.run(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        app_path
    ]
)