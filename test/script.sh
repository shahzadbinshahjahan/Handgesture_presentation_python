#!/bin/bash

for file in images/*.png;
do mv "$file" "${file%%-*}.png"
done
