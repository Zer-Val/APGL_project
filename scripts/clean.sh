#!/bin/bash

# CLEANING OF THE FILES USED FOR THE DASHBOARD
> /home/ubuntu/APGL_projet/docs/data.csv

# WE KEEP THE HEADERS FOR THE CSV FILES
echo "timestamp;value" > /home/ubuntu/APGL_projet/docs/data.csv
