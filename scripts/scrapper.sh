#!/bin/bash

URL="https://www.google.com/finance/quote/TSLA:NASDAQ"
DATA=$(curl -s -c cookies.txt "$URL")
PRICE=$(echo "$DATA" | grep -oP '<div class="YMlKec fxKbKc">\$[0-9,\.]+' | sed 's/<div class="YMlKec fxKbKc">//;s/\$//')

if [[ -n "$PRICE" ]]; then
	NEW_YORK_TIME=$(TZ="America/New_York" date "+%Y-%m-%d %H:%M:%S")
	echo "$NEW_YORK_TIME;$PRICE" >> /home/ubuntu/APGL_projet/docs/data.csv
else
	echo "ERROR : IMPOSSIBLE TO GATHER DATA FROM GOOGLE FINANCE"
fi
