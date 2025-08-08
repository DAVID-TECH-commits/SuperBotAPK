import subprocess
import sys

try:
    
    import sympy
    print("Sympy is already installed.")
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"])
    print("Sympy installed successfully!")
