#!/bin/bash

echo "Hello"
num=1
mkdir output
for file in images/*
do cp $file output/$num
	num=$((num+1))
done
