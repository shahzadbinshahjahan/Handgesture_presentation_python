#!/bin/bash

num=1
for file in images/*
do cp $file output/$num
	echo $file
	num=$((num+1))
done
