#!/bin/bash

echo -n "Please enter ppt name"
echo
read pptname
mkdir output/
mkdir tempoutput/
cp  $1 tempoutput/
cd tempoutput/
mkdir images/
echo "Converting presentation ..."
unoconv $pptname.pptx $pptname.pdf
echo "Doing final touches ..."
cd images/
convert ../$pptname.pdf i.png

#converting images to numbers for listing in python

num=1
for file in *
do cp $file ../../output/$num
	num=$((num+1))
done

#clearing all tempfiles
cd ../..
rm -r tempoutput/
echo "Thank you for your patience"
echo "Loading presentation"
python3 main.py "output/"


