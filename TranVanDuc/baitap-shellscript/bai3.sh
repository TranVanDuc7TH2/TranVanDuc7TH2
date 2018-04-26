#!/bin/bash
#Gan gia tri thoi gian cho bien 
gio=$(date +%H)  
echo "Bay gio la: $gio gio" 
if [[ $gio -ge 5 ]] && [[ $gio < 10 ]]
then
	echo "Chao buoi sang!"
else
	if [[ $gio = 10 ]] && [[ $gio -lt 15 ]]
	then
		echo "Chao buoi trua!"
	else
		if [[ $gio > 15 ]] && [[ $gio < 19 ]]
		then
			echo "Chao buoi chieu!"
		else 
			if [[ $gio -ge 19 ]] && [[ $gio < 22 ]]
			then
				echo "Chao buoi toi!"
			else
				echo "Dem khuya!"
			fi
		fi
	fi
fi


