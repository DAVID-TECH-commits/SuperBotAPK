import subprocess 
import sys

def install_buildozer():
    try:
        # Check if buildozer is already installed
        subprocess.run(["buildozer", "--version"], check=True)
        print("\n✅ Buildozer is already installed.")
    except:
        print("\n📦 Buildozer not found. Installing it now...\n")
        # Install using pip
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "buildozer"], check=True)
            print("\n✅ Buildozer has been successfully installed!")
        except subprocess.CalledProcessError:
            print("\n❌ Installation failed. Please check your internet connection or pip configuration.")

install_buildozer()
