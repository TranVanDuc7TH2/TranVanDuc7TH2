#!/bin/sh
echo - e " nhap ten file:"
read filename
if [ ! -f "$filename" ]; then
	echo " $filename not exists"
	exit 1
fi
answer=""
count=0
numlines=`wc -l $filename|sed 's/^ *//'|cut -d " " -f 1`
echo " so dong: $numlines"
while [ "$answer" != "n" ]
do
	echo "tiep tuc(y/n)?"
	read answer
	#kiem tra da doc het file chua
	if [ $count = $numlines ]; then
		echo "doc het file rui"
		exit 0
	fi
	#so dong da doc
	count=$(($count+1))
	#neu chon khong doc thi se khong in dong
	if [ "$answer" != "n" ]; then
		sed -n ${count}p $filename
	fi 
done
exit 0
