##########################################################################################
# Author: Dishanand Jayeprokash (Jay)
# Date Created: 16 July 2025
# Date Modified: 17 July 2025
##########################################################################################
# Note: 
# This script checks for missing and extra packages against a requirements.txt file.
# It logs missing packages to 'missing_packages.log' and extra packages to 'extra_packages.log'.
# It's a standalone utility for verifying package consistency, useful for development, testing, and deployment.
# Compatible with Python 3.6+, it uses argparse, pkg_resources, and logging.
# It does not install or modify packages; it only checks the current environment.
##########################################################################################
# command to run the script:
# python verify_requirements.py

# command to run the script with a custom requirements file:
# python verify_requirements.py --file "path/to/your/requirements.txt"


#################################### Version 3 ###########################################

import argparse       # parses command-line arguments
import pkg_resources     # accesses installed Python packages
import logging      # creates and manages log files

def parse_requirements(file_path):
    """
    Parse the requirements file to extract non-comment, non-empty lines.

    Args:
        file_path (str): Path to the requirements.txt file.

    Returns:
        list[str]: A list of package requirement strings.
    """
    try:
        with open(file_path, "r") as f:
            return [
                line.strip() for line in f
                if line.strip() and not line.strip().startswith("#")
            ]
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return []

def extract_package_name(requirement):
    """
    Extract the base package name from a requirement string, removing version specifiers.

    Args:
        requirement (str): A single package line from requirements.txt.

    Returns:
        str: The clean package name in lowercase.
    """
    return requirement.split("==")[0].split(">=")[0].split("<=")[0].strip().lower()

def log_to_file(filename, items):
    """
    Write a sorted list of packages to a log file.

    Args:
        filename (str): Path for the log file.
        items (list[str]): List of packages to log.

    Returns:
        None
    """
    with open(filename, "w") as f:
        for item in sorted(items):
            f.write(f"{item}\n")

def check_requirements(requirements_path="requirements.txt"):
    """
    Compare installed packages with those listed in the requirements file.
    Logs missing and extra packages conditionally.

    Args:
        requirements_path (str): Path to requirements.txt file.

    Returns:
        None
    """
    required = parse_requirements(requirements_path)
    if not required:
        return  # exit if the file couldn't be read or is empty

    required_pkg_names = [extract_package_name(pkg) for pkg in required]
    installed_pkgs = {pkg.key for pkg in pkg_resources.working_set}

    print("🔍 Checking installed packages...\n")

    missing = []
    installed_count = 0

    # compare required packages against installed packages
    for req in required:
        pkg_name = extract_package_name(req)
        if pkg_name in installed_pkgs:
            print(f"✅ Installed: {req}")
            installed_count += 1
        else:
            print(f"❌ Missing: {req}")
            missing.append(req)

    # find installed packages that are not in the requirements file
    extra = [pkg for pkg in installed_pkgs if pkg not in required_pkg_names]

    
    print(f"\n📊 Installed packages found from requirements.txt: {installed_count}/{len(required)}")
    print(f"📦 Additional packages installed: {len(extra)}")

    # log missing packages only if any
    if missing:
        log_to_file("missing_packages.log", missing)
        print("📝 Missing packages logged to 'missing_packages.log'")
    else:
        print("🎉 No missing packages. No log file created.")

    # log extra installed packages only if any
    if extra:
        log_to_file("extra_packages.log", extra)
        print("📝 Extra packages logged to 'extra_packages.log' \n")
    else:
        print("🧼 No extra packages. No log file created. \n")

if __name__ == "__main__":
    """
    Entry point for command-line execution.
    Parses an optional argument --file to specify a custom requirements file.
    """
    parser = argparse.ArgumentParser(description="Verify Python package requirements.")
    parser.add_argument("--file", default="requirements.txt", help="Path to requirements file")
    args = parser.parse_args()
    check_requirements(args.file)


