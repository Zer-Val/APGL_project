#!/bin/bash

INPUT_CSV="/home/ubuntu/APGL_projet/docs/data.csv"
OUTPUT_CSV="/home/ubuntu/APGL_projet/docs/rapport.csv"

PRICES=$(awk -F';' 'NR>1 {print $2}' "$INPUT_CSV")

MAX_VALUE=$(echo "$PRICES" | sort -nr | head -n1)
MIN_VALUE=$(echo "$PRICES" | sort -n | head -n1)
OPENING_VALUE=$(awk -F';' '$1 ~ / 09:30/ {print $2; exit}' "$INPUT_CSV")
CLOSING_VALUE=$(awk -F';' '$1 ~ / 16:00/ {print $2; exit}' "$INPUT_CSV")

echo "$OPENING_VALUE;$MIN_VALUE;$MAX_VALUE;$CLOSING_VALUE" >> "$OUTPUT_CSV"
echo "rapport fait"
