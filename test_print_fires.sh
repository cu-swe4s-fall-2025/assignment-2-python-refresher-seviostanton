#!/bin/bash
set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed
# fetch ssshtest if missing, then source it
[ -f ssshtest ] || (curl -fsSL -o ssshtest https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest || wget -q -O ssshtest https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest || { echo "Missing curl/wget. Commit ssshtest to the repo."; exit 1; })
. ssshtest

# test -e ssshtest || wget -qhttps://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
# . ssshtest

# ---- script, data, parameters ----
SCRIPT=print_fires.py
DATA=Agrofood_co2_emission_tiny.csv

COUNTRY="Italy"
COUNTRY_COLUMN=0
FIRES_COLUMN=7

#expected outputs for Zimbabwe
EXPECTED_RAW="Values from column 7 for Italy: [1744, 1603, 1571, 1398]"
EXPECTED_MEAN="mean of values from column 7 for Italy: 1579.0"
EXPECTED_MEDIAN="median of values from column 7 for Italy: 1587.0"
EXPECTED_STD="std of values from column 7 for Italy: 142.15718999286202"
EXPECTED_FILE_NOT_FOUND="Error: File 'does_not_exist.csv' not found."

# ---- tests ----
run raw_data python3 $SCRIPT --file_name $DATA --country "$COUNTRY" --country_column $COUNTRY_COLUMN --fires_column $FIRES_COLUMN
assert_exit_code 0
assert_in_stdout "$EXPECTED_RAW"

run mean_data python3 $SCRIPT --file_name $DATA --country "$COUNTRY" --country_column $COUNTRY_COLUMN --fires_column $FIRES_COLUMN --operation "mean"
assert_exit_code 0
assert_in_stdout "$EXPECTED_MEAN"

run median_data python3 $SCRIPT --file_name $DATA --country "$COUNTRY" --country_column $COUNTRY_COLUMN --fires_column $FIRES_COLUMN --operation "median"
assert_exit_code 0
assert_in_stdout "$EXPECTED_MEDIAN"

run std_data python3 $SCRIPT --file_name $DATA --country "$COUNTRY" --country_column $COUNTRY_COLUMN --fires_column $FIRES_COLUMN --operation "std"
assert_exit_code 0
assert_in_stdout "$EXPECTED_STD"

run no_country python3 $SCRIPT --file_name $DATA --country "Narnia" --country_column $COUNTRY_COLUMN --fires_column $FIRES_COLUMN
assert_exit_code 0
assert_in_stdout "Values from column $FIRES_COLUMN for Narnia: []"

run missing_file python3 "$SCRIPT" --file_name does_not_exist.csv --country "$COUNTRY" --country_column $COUNTRY_COLUMN --fires_column $FIRES_COLUMN
assert_exit_code 1
assert_in_stderr "$EXPECTED_FILE_NOT_FOUND"