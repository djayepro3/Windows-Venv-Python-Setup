# 🧰 Python Virtual Environment Setup on Windows (Deep Learning Ready)

> 📌 **Author:** Dishanand Jayeprokash  
> 🗓️ **Created:** 17 July 2025  
> ✏️ **Last Modified:** 22 July 2025  
> 📘 **Covers:** Virtual Environment Setup • VS Code Integration • Package Installation • Requirements Management

---

<p align="center">
  <img src="images/python_logo.png" alt="Python Logo" width="100"/>
  &nbsp;&nbsp;&nbsp;
  <img src="images/vscode_logo.png" alt="VS Code Logo" width="100"/>
</p>

---
## 📚 Table of Contents

1. [🌐 Create a Virtual Environment](#-create-a-virtual-environment)
2. [⚡ Activate the Environment](#-activate-the-environment)
3. [🧭 Select Interpreter in VS Code](#-select-interpreter-in-vs-code)
4. [📦 Install Required Packages](#-install-required-packages)
5.  [📂 Sample `requirements.txt`](#-sample-requirementstxt)
6. [🧪 Verify Package Installation](#-verify-package-installation)
8. [📉 Deactivate Virtual Environment](#-deactivate-virtual-environment)
9. [🎉 Conclusion](#-conclusion)
10. [📘 Detailed Setup Reference](#-detailed-setup-reference)
11. [📬 Feedback](#-feedback)


---

## 🌐 Create a Virtual Environment

Open your terminal and run:

```bash
python -m venv venv
````

This creates a folder named `venv` which contains your isolated Python environment.

> ℹ️ `python -m venv` uses the built-in `venv` module to set up the environment.

---

## ⚡ Activate the Environment

In the terminal (PowerShell or Command Prompt):

```bash
venv\Scripts\activate
```

> 🛡️ **Execution Policy Error?**
> If you see something like:

```
venv\scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system.
```

🔧 Fix it by running:

```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

---

## 🧭 Select Interpreter in VS Code

1. Open **Command Palette**: `Ctrl + Shift + P`
2. Type: `Python: Select Interpreter`
3. Choose the one that points to:

   ```
   .\venv\Scripts\python.exe
   ```

✅ This ensures VS Code uses your virtual environment.

---

## 📦 Install Required Packages

To install packages:

```bash
pip install torch
```

Or use a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This is more scalable and version-controlled.

---

## 📂 Sample `requirements.txt`

Create a new file to the current directory and save it as requirements.txt. Copy paste the following, save it, and install it as shown above:

```txt
torch>=2.0.0
torchvision>=0.15.0
numpy
matplotlib
opencv-python
Pillow
tifffile
rasterio
scikit-image
geopandas
pyproj
tqdm
```

### 🔍 Why These Packages?

| Package                   | Purpose                    |
| ------------------------- | -------------------------- |
| `torch`, `torchvision`    | Deep learning              |
| `numpy`, `matplotlib`     | Arrays & plotting          |
| `opencv-python`, `Pillow` | Image loading & processing |
| `tifffile`, `rasterio`    | TIFF/GeoTIFF support       |
| `scikit-image`            | Extra image processing     |
| `geopandas`, `pyproj`     | Geospatial metadata        |
| `tqdm`                    | Progress bars for loops    |

---


## 🧪 Verify Package Installation

You can check installed packages with:

```bash
pip list
```

> ❌ But this is tedious for long lists. So...

### ✅ Use a verification script:

Run the included script:

```bash
python verify_requirements.py
```

It will:

* ✅ Validate installed packages and versions
* 📝 Log missing packages to `missing_packages.log`
* 📦 Log extra packages to `extra_packages.log`
* 💡 Show install summary

---

## 📉 Deactivate Virtual Environment

When done:

```bash
deactivate
```

### ✅ Why deactivate?

* Resets your shell to system Python
* Avoids accidental installs into the wrong env
* Keeps your project tidy
* Helps when switching between multiple projects

---

## 🎉 Conclusion

You now have a clean, portable Python environment ready for deep learning and geospatial processing on Windows!

> 💡 Use this setup to power your preprocessing pipelines, generative models, or inference tools in an isolated and reproducible way.

---

## 📘 Detailed Setup Reference

📄 For a more detailed walkthrough with step-by-step commands and background info, check out:  
[**Win_venv.txt**](setup/create_Venv_Windows.txt)

This text file includes:
- How to create and activate a virtual environment
- Common errors and their fixes (e.g., PowerShell script execution)
- How to choose interpreters in VS Code
- Package installation techniques and reasoning
- Full explanation of package roles for ML and geospatial work
- A custom script (`verify_requirements.py`) to track missing/extra packages

> 🧠 Use this as your offline cheat sheet or printout!

---

## 📬 Feedback

Have suggestions or want to contribute?
Feel free to **fork the repo**, open an **issue**, or submit a **pull request**.

---

## 📦 Clone This Repo

```bash
git clone https://github.com/djayepro3/Windows-Venv-Python-Setup
cd Windows-Venv-Python-Setup
```
