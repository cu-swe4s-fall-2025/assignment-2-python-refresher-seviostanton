# Assignment 3: Best Practices

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
print_fires.py dependencies only include `sys`, `argparse`, and the `my_utils.py` library included in the repo. 
However, the complete dev environment used at time of production has been included in the swe4s_env.yml

## 5) MIT License
Copyright 2025 Sevio Stanton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.