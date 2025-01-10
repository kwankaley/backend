import subprocess
import sys
import json

ALLOWED_LICENSES = [
    "MIT",
    "BSD",
    "Apache 2.0",
    "ISC",
    "LGPL",
    "Public Domain"
]

def check_python_licenses():
    print("Installing Python dependencies...")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

    print("Running pip-licenses...")
    result = subprocess.run(
        ["pip-licenses", "--format=json"],
        capture_output=True,
        text=True,
        check=True
    )

    licenses = json.loads(result.stdout)

    disallowed_packages = [
        package for package in licenses
        if package["License"] not in ALLOWED_LICENSES
    ]

    if disallowed_packages:
        print("Disallowed licenses found:")
        for package in disallowed_packages:
            print(f"Package: {package['Name']}, License: {package['License']}")
        sys.exit(1)

    print("All licenses are allowed.")

if __name__ == "__main__":
    try:
        check_python_licenses()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)
    print("Python license check completed successfully.")

