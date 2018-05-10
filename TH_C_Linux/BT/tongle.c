#include <stdio.h>
int tongle(int n)
{
	int tong = 0;
	int i;
	for (i=1; i <= n; i++)
		if (i % 2 != 0)
			tong = tong + i;
	return tong;
}

