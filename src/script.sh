#!/bin/bash


#gets the file name from the path
fullpath=$1
filename=$(basename ${fullpath})
#echo $filename
#output is filename.extension

#removing extension
xpath=${fullpath%/*}
xbase=${fullpath##*/}
xfext=${xbase##*.} #this stores the file extension
pptname=${xbase%.*} #this stores the filename without extension
#echo $pptname

#echo -n "Please enter ppt name"
#echo
#read pptname
#ls

if [ -d "/home/shah/Documents/projects/opencv/Handgesture_presentation_python/Resources/$pptname/images" ];
then
	echo "Loading Presentation into Handy PPT"
elif [ "$xfext" == "pdf" ]
then
	mkdir /home/shah/Documents/projects/opencv/Handgesture_presentation_python/Resources/$pptname
	cd /home/shah/Documents/projects/opencv/Handgesture_presentation_python/Resources/$pptname/
	cp  $1 .
	mkdir images/
	cd images/
   	convert ../$pptname.pdf i.png
	for file in *.png;
    		do mv $file "$(echo $file | cut -c 3- | rev | cut -c 5- | rev)"
        done
   	cd /home/shah/Documents/projects/opencv/Handgesture_presentation_python/src/


else	
    mkdir /home/shah/Documents/projects/opencv/Handgesture_presentation_python/Resources/$pptname
    #copying the presentation from the input path to temporary folder
    cd /home/shah/Documents/projects/opencv/Handgesture_presentation_python/Resources/$pptname/
    cp  $1 .
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
    cd /home/shah/Documents/projects/opencv/Handgesture_presentation_python/src/
fi

echo "Thank you for your patience"
echo "Loading presentation"


#ls
#echo $pptname
python3 main.py /home/shah/Documents/projects/opencv/Handgesture_presentation_python/Resources/$pptname/images
