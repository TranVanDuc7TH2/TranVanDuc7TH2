#!/bin/bash
clear 
echo "----------------------------"
echo "-------Menu lua chon--------"
echo "----------------------------"
echo "1. Cafe den"
echo "2. Cafe da"
echo "3. Cafe sua"
echo "4. Cafe ca cao"
echo "----------------------------"
echo "Ban chon thuc uong nao(1-4): "
read lc
case $lc in
"1")
	echo "Ban chon: Cafe den ";;
"2")
	echo "Ban chon: Cafe da ";;
"3")
	echo "Ban chon: Cafe sua ";;
"4")
	echo "Ban chon: Cafe ca cao";;
esac 
