#!/bin/bash

set -e  # stop on error
set -u  # raise error if variable is unset
set -o pipefail  # fail if any prior step failed

echo "Running print_fires.py"
echo "======================================================"
echo "Example 1: Successful Run"
python3 print_fires.py \
  --file_name Agrofood_co2_emission.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 1

echo "------------------------------------------------------"
echo "Example 2: Failed Run; Missing Data"
python3 print_fires.py \
  --file_name oopsies.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 2 || True # prevent exit on error for this command

echo "------------------------------------------------------"
echo "Example 3: Failed Run; Calling int() on wrong data type"
python3 print_fires.py \
  --file_name Agrofood_co2_emission.csv \
  --country "United States of America" \
  --country_column 0 \
  --fires_column 2