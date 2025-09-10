#!/bin/bash

python3 print_fires.py \
  --file Agrofood_co2_emission.csv \
  --country_name "United States of America" \
  --country_column 0 \
  --fires_column 2
