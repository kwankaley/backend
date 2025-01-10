import subprocess
import sys

def check_python_licenses():
    print("Installing Python dependencies...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

    print("Running pip-licenses...")
    subprocess.run([
        "pip-licenses",
        "--format=json",
        "--output-file=python_licenses.json",
        "--fail-on",
        "Proprietary,AGPL"
    ], check=True)

if __name__ == "__main__":
    try:
        check_python_licenses()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print("Python license check completed successfully.")
