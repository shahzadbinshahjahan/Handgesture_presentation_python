#!/bin/bash

echo "Hello"
num=1
mkdir output
for file in $1
do cp $file output/$num
	num=$((num+1))
done
