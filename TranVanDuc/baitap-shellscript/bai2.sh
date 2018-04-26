#!/bin/bash
read -p "Nhap ho (Viet hoa chu cai dau): " ho
read -p "Nhap ten (Viet hoa chu cai dau): " ten
if [ $ho = "Tran" ] && [ $ten = "Duc" ]
then
	echo "Trung khop"
else
	echo "Khong trung khop"
fi 
