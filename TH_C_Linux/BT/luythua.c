#include <stdio.h>
int luythua(int x, int n)
{
	if (n == 0)
		return 1;
	else
	{
		int lt = 1;
		int i;
		for (i = 1; i <= n; i++)
			lt = lt * x;
		return lt;
	}
}

