#!/bin/bash

# CLEAN THE FILES
> /home/ubuntu/APGL_projet/docs/data.csv
> /home/ubuntu/APGL_projet/docs/rapport.csv
> /home/ubuntu/APGL_projet/docs/volatility.txt

# ADD THE HEADERS FOR THE FILES FOR THE GRAPH
echo "timestamp;value" > /home/ubuntu/APGL_projet/docs/data.csv
