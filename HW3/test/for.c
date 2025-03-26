// 范權榮 111210557
#include <stdio.h>

// sum(n) = 1+2+...+n
int sum(int n)
{
  int s, i;
  s = 0;
  for (i = 1; i <= n; i++)
  {
    s = s + i;
  }
  return s;
}

int main()
{
  printf("sum(20)=%d\n", sum(20));
  return 0;
}
