#!/bin/bash

#gets the file name from the path
#fullpath=$1
#filename=$(basename ${fullpath})
#echo $filename
#output is filename.extension

#removing extension
#xpath=${fullpath%/*}
#xbase=${fullpath##*/}
# xfext=${xbase##*.} this stores the file extension 
#xpref=${xbase%.*} #this stores the filename without extension
#echo $xpref
#mkdir $xpref

#!/bin/bash

# using [ expression ] syntax and in place 
# of File.txt you can write your file name 
filename=File
if [ -d "$filename/images" ]; 
then

# if file exist the it will be printed 
echo "File is does  exist"
else

# is it is not exist then it will be printed
echo "File is does not exist"
fi
