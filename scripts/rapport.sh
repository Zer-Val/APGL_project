#!/bin/bash

# DEFINITION OF THE INPUT AND THE OUTPUT FILES PATH
INPUT_CSV="/home/ubuntu/APGL_projet/docs/data.csv"   # FILE PATH FOR THE INPUT FILe
OUTPUT_CSV1="/home/ubuntu/APGL_projet/docs/rapport.csv" # FILE PATH FOR THE OUTPUT FILE : REPORT OF THE DAY
OUTPUT_CSV2="/home/ubuntu/APGL_projet/docs/data_history.csv" #FILE PATH FOR THE OUTPUT FILE : DATA HISTORY OF THE MARKET 


if [ ! -f "$INPUT_CSV" ]; then # TRIGGERED IF THE INPUT FILE DOES NOT EXIST OR IS NOT A REGULAR FILE
    echo "ERROR: FILE NOT FOUND."
    exit 1
fi

# EXTRACT THE PRICES BUT NOT THE HEADER
PRICES=$(awk -F';' 'NR>1 {print $2}' "$INPUT_CSV")

# FIND THE MAX AND MIN VALUES OF THE STOCK PRICE
MAX_VALUE=$(echo "$PRICES" | sort -nr | head -n1) #SORT THE VALUES BY DECREASING ORDER AND TAKES THE FIRST ONE (THE MAX)
MIN_VALUE=$(echo "$PRICES" | sort -n | head -n1) #SORT THE VALUES BY INCREASING ORDER AND TAKES THE FIRST ONE (THE MIN)

# TAKES THE VOLATILITY GUVEN BY THE VOLATILITY SCRIPT
VOLATILITY=$(cat /home/ubuntu/APGL_projet/docs/volatility.txt) # READ THE DATA FROM THE VOLATILITY.TXT FILE CREATED BY THE VOLATILITY SCRIPT

# EXTRACT THE OPENING VALUE OF THE STOCK (OPENING = 09:30 AM ET)
OPENING_VALUE=$(awk -F';' '$1 ~ / 09:30/ {print $2; exit}' "$INPUT_CSV") #
# EXTRACT THE CLOSING VALUE OF THE STOCK (CLOSING = 04:00 PM ET)
CLOSING_VALUE=$(awk -F';' '$1 ~ / 16:00/ {print $2; exit}' "$INPUT_CSV") # THE SYSTEM REGISTERS WITH A 24 HOURS FORMAT SO WE USE THIS FORMAT HERE

# MAKES SURE THAT WE HAVE ALL THE EXPECTED VALUES FOR THE REPORT
if [ -z "$OPENING_VALUE" ] || [ -z "$MIN_VALUE" ] || [ -z "$MAX_VALUE" ] || [ -z "$VOLATILITY" ] || [ -z "$CLOSING_VALUE" ]; then
	echo "ERROR : SOME VALUES ARE MISSING"
	exit 1
fi

# PRODUCES THE REPORT OF THE DAY AS A CSV
echo "$OPENING_VALUE;$MIN_VALUE;$MAX_VALUE;$CLOSING_VALUE;$VOLATILITY" >> "$OUTPUT_CSV1"

# SAVES THE DAILY REPORT DATA IN A HISTORY CSV
DATE=$(date +%Y-%m-%d) # DATE WITH THE YYYY-MM-DD FORMAT
echo "$DATE;$OPENING_VALUE;$MIN_VALUE;$MAX_VALUE;$CLOSING_VALUE;$VOLATILITY" >>  "$OUTPUT_CSV2"

# INFORMS THE DEV THAT THE DAY'S REPORT IS AVAILABLE (à retirer ?) 
echo "DAILY REPORT OF THE DAY PRODUCED CORRECTLY"
