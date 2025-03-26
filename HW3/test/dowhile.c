// 范權榮 111210557
#include <stdio.h>
int sum(int n)
{
	int i, s;
	i = 0;
	s = 0;

	do
	{
		s = s + i;
		i++;
	} while (i <= n);

	return s;
}

int main()
{
	printf("sum(12)=%d\n", sum(12));
	return 0;
}