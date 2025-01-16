import subprocess
import sys
import json

ALLOWED_LICENSES = [
    "MIT License",
    "BSD License",
    "Apache 2.0",
    "ISC",
    "LGPL",
    "Public Domain"
]

def load_allowed_licenses(config_path):
    with open(config_path, "r") as config_file:
        config = json.load(config_file)
    return config.get("allowedLicenses", [])

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
    allowed_licenses = load_allowed_licenses("./licenses_config.json")

    disallowed_packages = [
        package for package in licenses
        if package["License"] not in allowed_licenses
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

