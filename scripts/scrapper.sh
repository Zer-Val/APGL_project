#!/bin/bash

DATA=$(curl "https://www.google.com/finance/quote/TSLA:NASDAQ")
PRICE=$(echo "$DATA" | grep -oP '(\d+\.\d+)(?=\s*&nbsp;\$)' )
TIME=$(date "+%Y-%m-%d %H:%M:%S")

echo "$TIME;$PRICE" >> ../docs/data.csv
