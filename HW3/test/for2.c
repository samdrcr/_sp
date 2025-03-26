// 范權榮 111210557
#include <stdio.h>

int sum(int n)
{
  int s, i;
  s = 0;
  printf("s=%d\n", s);
  for (i = 1; i <= n; i++)
  {
    printf("start:i=%d s=%d\n", i, s);
    s = s + i;
    printf("end:i=%d s=%d\n", i, s);
  }
  return s;
}

int main()
{
  printf("sum(20)=%d\n", sum(20));
  return 0;
}
