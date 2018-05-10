#include <stdio.h>
int giaithua(int n)
{
	if (n == 0)
		return 1;
	else
	{
		int gt=1;
		int i;
		for (i=1; i <=n; i++)
			gt = gt * i;
		return gt;
	}
}
