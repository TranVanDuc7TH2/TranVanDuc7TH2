n=int(input("Nhap so phan tu cua mang: "))
#Khai bao mang
a=[]
for i in range(n):
	print "Nhap phan tu thu: ",i+1
	a.append(input())
#In ra day so vua nhap
print "Day so vua nhap: "
print a
tong = 0;
#Tim phan tu chan
print "Cac phan tu chan cua mang: "
for i in range(n):
	if a[i]%2==0:
		print a[i]
		tong=tong+a[i]
print "Tong cac phan tu chan: ", tong

