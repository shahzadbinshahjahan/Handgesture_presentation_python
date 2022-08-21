#!/bin/bash

for file in *.png;
do mv $file "$(echo $file | cut -c 3- | rev | cut -c 5- | rev)"
done
