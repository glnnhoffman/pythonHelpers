# Migrating from the Default Conda Channel to conda-forge

## Why Migrate to conda-forge?
- **More up-to-date packages**: conda-forge often has newer versions.
- **Wider package availability**: Includes many packages not available in the default `defaults` channel.
- **Community maintained**: Broad and active contributor base.
- **Consistent builds**: Packages are built in a unified environment for compatibility.

---

## Step 1: Configure Conda to Use conda-forge
To prioritize `conda-forge`, update your Conda configuration:

```sh
conda config --add channels conda-forge
conda config --set channel_priority strict
```

This will:
- Add `conda-forge` to your channel list
- Enforce strict channel priority to avoid mixing packages from different channels

To verify:
```sh
conda config --show channels
conda config --show channel_priority
```

---

## Step 2: Update Existing Environment to Use conda-forge Packages
To switch an existing environment to use packages from `conda-forge`, do the following:

### Option A: Create a new environment from scratch
1. Export your current environment:
   ```sh
   conda list --explicit > spec-file.txt
   ```
2. Edit `spec-file.txt` and remove any lines that reference the `defaults` channel.
3. Create a new environment:
   ```sh
   conda create --name new_env_name --file spec-file.txt
   ```

### Option B: Recreate environment using environment.yml
1. Export your environment to YAML:
   ```sh
   conda env export --from-history > environment.yml
   ```
2. Edit `environment.yml` to include:
   ```yaml
   channels:
     - conda-forge
   channel_priority: strict
   ```
3. Recreate the environment:
   ```sh
   conda env create -n new_env_name -f environment.yml
   ```

---

## Step 3: Update Packages to conda-forge Versions
To upgrade an existing environment to conda-forge packages:
```sh
conda update --all
```
This will attempt to replace current packages with versions from `conda-forge`, respecting strict channel priority.

If conflicts occur, consider removing and reinstalling problematic packages one by one.

---

## Step 4: Set conda-forge as Default for All Environments (Optional)
To apply `conda-forge` and strict priority globally:
```sh
conda config --add channels conda-forge
conda config --set channel_priority strict
```
This ensures that future environments use `conda-forge` by default.

---

## Step 5: Verify Installation Sources
To check which channel a package came from:
```sh
conda list
```
Packages installed from `conda-forge` will be labeled accordingly in the "channel" column.

---

## Summary
1. **Add conda-forge and enable strict priority.**
2. **Export and recreate environments referencing conda-forge.**
3. **Update packages to transition to conda-forge versions.**
4. **Optionally set conda-forge as default for future use.**
5. **Check installed package sources for verification.**

Migrating to `conda-forge` improves access to the latest, well-maintained packages and improves reproducibility in complex environments.
