#!/bin/bash

INPUT_CSV="/home/ubuntu/APGL_projet/docs/data.csv"

if [ ! -f "$INPUT_CSV" ]; then
	echo "ERROR: FILE NOT FOUND"
	exit 1
fi

PRICES=$(awk -F';' 'NR>1 {print $2}' "$INPUT_CSV")

SUM=0
SUM_SQ=0
COUNT=0

for PRICE in $PRICES; do
	SUM=$(echo "$SUM+$PRICE" | bc)
	COUNT=$((COUNT+1))
done

if [ "$COUNT" -eq 0 ]; then
	echo "ERROR: NO PRICE FOUND"
	exit 1
fi

MEAN=$(echo "scale=5; $SUM/$COUNT" | bc)

for PRICE in $PRICES; do
	DIFF=$(echo "$PRICE - $MEAN" | bc)
	SQUARE=$(echo "$DIFF * $DIFF" | bc)
	SUM_SQ=$(echo "$SUM_SQ + $SQUARE" | bc)
done

VARIANCE=$(echo "scale=5; $SUM_SQ/$COUNT" | bc)
VOLATILITY=$(echo "scale=5; sqrt($VARIANCE)" | bc -l)

echo "$VOLATILITY" > /home/ubuntu/APGL_projet/docs/volatility.txt
