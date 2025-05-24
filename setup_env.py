import subprocess
import sys
import os

def create_environment():
    # Create a virtual environment
    subprocess.run([sys.executable, "-m", "venv", "phi_env"])
    
    # Determine the pip path based on OS
    pip_path = os.path.join("phi_env", "Scripts", "pip") if os.name == "nt" else os.path.join("phi_env", "bin", "pip")
    
    # Upgrade pip first
    subprocess.run([pip_path, "install", "--upgrade", "pip"])
    
    # Install phidata with the correct Pydantic version
    subprocess.run([pip_path, "install", "pydantic>=2.0.0"])  # Install Pydantic v2+
    subprocess.run([pip_path, "install", "phidata"])  # Install phidata after correct Pydantic
    
    print("Environment created successfully. Activate with:")
    if os.name == "nt":
        print(r"phi_env\Scripts\activate")
    else:
        print("source phi_env/bin/activate")



if __name__ == "__main__":
    create_environment()