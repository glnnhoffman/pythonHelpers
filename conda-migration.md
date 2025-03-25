# Migrating from Anaconda to Standard Python with venv

## Step 1: Install Standard Python
If you haven’t already installed standard Python:
1. **Download and install Python** from [python.org](https://www.python.org/downloads/).
2. Ensure you check **"Add Python to PATH"** during installation.

To verify the installation, run:
```sh
python --version
pip --version
```

---

## Step 2: Identify Your Current Conda Environment Dependencies
To recreate your Conda environment, you need a list of installed packages:
```sh
conda list --export > conda_packages.txt
```
This will output all packages, but since Conda includes system-level dependencies, we should filter only Python packages.

To generate a standard `requirements.txt`:
```sh
conda list --export | grep -E "^(?!#|@)" | awk -F= '{print $1"=="$2}' > requirements.txt
```
Alternatively, you can manually install only the necessary packages.

---

## Step 3: Create a Virtual Environment with venv
1. Navigate to your project folder:
   ```sh
   cd /path/to/project
   ```
2. Create a new virtual environment:
   ```sh
   python -m venv venv
   ```
3. **Activate the virtual environment:**
   - **Windows:**
     ```sh
     venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```sh
     source venv/bin/activate
     ```

To confirm activation, check that `(venv)` appears in the terminal prompt.

---

## Step 4: Install Packages with Pip
Use the generated `requirements.txt` to install necessary packages:
```sh
pip install -r requirements.txt
```

If you need Jupyter support (previously handled by Conda):
```sh
pip install jupyterlab
```

### Option B: Install from pyproject.toml
To install a package containing a `pyproject.toml` file:

```sh
pip install .
```
If you want the package to be editable:
```sh
pip install -e . 
```

> Make sure you're in your project directory with a valid `pyproject.toml` before running these commands.

---

## Step 5: Set Up VS Code for the Virtual Environment
1. Open VS Code.
2. Install the **Python extension** (if not already installed).
3. Open the **Command Palette** (`Ctrl + Shift + P` / `Cmd + Shift + P` on Mac).
4. Search for **"Python: Select Interpreter"** and select your `venv` interpreter.
   - The path should be something like:
     ```
     .venv/bin/python (Mac/Linux)
     .venv\Scripts\python.exe (Windows)
     ```

---

## Step 6: Remove Anaconda from Path (Optional)
If you want to stop using Anaconda completely:
1. Remove Anaconda from your system’s `PATH` environment variable.
2. Uninstall Anaconda (optional) via:
   - Windows: Use **"Add or Remove Programs"**.
   - Mac/Linux: Run `rm -rf ~/anaconda3` (or `miniconda3`).

---

## Step 7: Test and Adjust
- Run a script to ensure everything is working:
  ```sh
  python your_script.py
  ```
- If you miss any packages, install them manually with:
  ```sh
  pip install package-name
  ```

---

## Summary
1. **Install standard Python** and add it to `PATH`.
2. **Export Conda dependencies** and convert them to `requirements.txt`.
3. **Create a virtual environment** using `venv`.
4. **Activate the environment** and install packages with `pip`.
5. **Set up VS Code** to use the new environment.
6. **(Optional) Remove Anaconda from `PATH` or uninstall it**.
7. **Test and refine your new setup**.

This transition simplifies environment management and improves portability while keeping the benefits of virtual environments. 🚀
