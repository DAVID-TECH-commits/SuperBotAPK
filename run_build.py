import os 
import subprocess

# Set working directory
os.chdir("C:/Users/David Adeola/Desktop/DavidAPKBuild")  # CHANGE THIS to your folder path

# Run the buildozer build command
build_command = "buildozer -v android debug"

try:
    subprocess.run(build_command, shell=True)
    print("APK build process started...")
except Exception as e:
    print("Error running Buildozer:", e)
