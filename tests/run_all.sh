#!/bin/bash

clear
for i in $(ls *.py); do
    echo "Running $i..."
    ./$i
done
