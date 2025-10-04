# Assignments 2-5

## 1) What this project does
This project implements a command-line tool, `print_fires.py`, that reads a CSV file and prints values from a specified column for rows matching a given country.  
It demonstrates software engineering best practices:
- `argparse` for argument parsing
- `main()` entry point
- Uses exit codes for error handling
- Docstrings and comments
- Includes example shell script (`run.sh`) with successful and failing runs

---

## 2) How to install it
a) Clone the repository from GitHub
git clone <repo-url>
cd <repo-name>

b) Get the data file to follow the example runs exactly: https://drive.google.com/drive/folders/1voRNzPWjvohrjAEMvKjdQ71qu_j15pBj?usp=drive_link
and place in the same directory as print_fires.py

## 3) Example Usage
In the command line use `./run.sh` to run the included bash script showing one successful run and two failed runs (make script executable: `chmod +x run.sh`)

## 4) Dev Environment
print_fires.py dependencies only include `python` and the `my_utils.py` library included in the repo. 
However, a complete environment has been provided:  `environment.yml`

## 5) Summary of Changes for Assignment 5 
- Added continuous integration (CI) with **mamba-org/setup-micromamba** and a portable `environment.yml` (`conda-forge`; `Python`, `numpy`, `pycodestyle`, `pytest`).
- Added **MIT LICENSE**.
- Removed stdlib modules (`argparse`, `sys`, `unittest`) from env deps; they’re provided by Python.
- Ensured style checks (PEP8 via `pycodestyle`), unit tests, and functional tests run locally and in CI.
