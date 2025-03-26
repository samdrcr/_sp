// 范權榮 111210557
#include <stdio.h>

int sum(int n)
{
  int s;
  int i;
  s = 0;
  i = 1;
  while (i <= n)
  {
    s = s + i;
    i++;
  }
  return s;
}

int main()
{
  printf("sum(20)=%d\n", sum(20));
  return 0;
}
