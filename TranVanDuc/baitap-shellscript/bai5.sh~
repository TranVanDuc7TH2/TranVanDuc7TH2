#Xoa man hinh 
clear 
echo "----------------------------"
echo "----Cac phep toan so hoc----"
echo "----------------------------"
echo "Phep cong (+)"
echo "Phep tru (-)"
echo "Phep nhan (*)"
echo "Phep chia (/)"
echo "Ket thuc (q)"
echo "----------------------------"
echo "Moi chon: "
read lc
if [ $lc != q ]
then 
	echo "Moi nhap a"
	read a
	echo "Moi nhap b"
	read b 
fi 
case $lc in
"+")
	echo "Tong hai so:"
	let "kq=$a+$b"
	echo $kq;;
"-")
	echo "Hieu hai so:" 
	let "kq=$a-$b"
	echo $kq;;
"*")
	echo "Tich hai so:" 
	let "kq=$a*$b"
	echo $kq;;
"/")
	if [ $b = 0 ]
	then 
		echo "Khong the chia cho 0"
	else	
		echo "Thuong hai so:" 
		let "kq=$a/$b"
		echo $kq
	fi ;;
"q")
	echo "Ban da chon thoat chuong trinh" 
	echo "Da thoat chuong trinh" 
	exit
esac 
