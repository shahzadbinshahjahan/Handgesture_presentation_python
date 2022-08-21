#!/bin/bash

echo -n "Please enter ppt name"
echo
read pptname

mkdir tempoutput/
#copying the presentation from the input path to temporary folder
cp  $1 tempoutput/
cd tempoutput/
mkdir images/
echo "Converting presentation ..."
unoconv $pptname.pptx $pptname.pdf
echo "Doing final touches ..."
cd images/
convert ../$pptname.pdf i.png

#depreceated - converting images to numbers for listing in python
#as linux is not listing in numerical order

#num=1
#for file in *
#do cp $file ../../output/$num
#	num=$((num+1))
#done

#converting image names to only number for listing in python
#input each file in whatever order they are in
#removes the first two character i.e "i-"
#reverses it , i.e "10.png" wil be "gnp.01"
#removes the first 4 chars from the reversed string, output: 01"
#reverse it again to get the proper number, i.e: 01 will be 10"
for file in *.png;
do mv $file "$(echo $file | cut -c 3- | rev | cut -c 5- | rev)"
done

echo "Thank you for your patience"
echo "Loading presentation"
python3 main.py "tempoutput/images/"


