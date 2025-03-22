#!/bin/bash

#DEFINE THE URL WHERE WE GATHER DATA
URL="https://www.google.com/finance/quote/TSLA:NASDAQ"

# COLLECT THE PAGE CODE FROM THE URL DEFINED
DATA=$(curl -s -c cookies.txt "$URL")

# GET THE ARRAYS OF 6 NUMBERS FROM THE CODE
PRICE=$(echo "$DATA" | grep -oP '<div class="YMlKec fxKbKc">\$[0-9,\.]+' | sed 's/<div class="YMlKec fxKbKc">//;s/\$//')

# VERIFY THAT THERE ARE ARRAYS COLLECTED
if [[ -n "$PRICE" ]]; then
	NEW_YORK_TIME=$(TZ="America/New_York" date "+%Y-%m-%d %H:%M:%S") # DEFINE THE TIMESTAMP (ET)
	echo "$NEW_YORK_TIME;$PRICE" >> /home/ubuntu/APGL_projet/docs/data.csv # ADD THE TWO DATA TO the CSV FILE
else
	echo "ERROR : IMPOSSIBLE TO GATHER DATA FROM GOOGLE FINANCE"
fi
