// 范權榮 111210557
#include <stdio.h>

int f(int n)
{
  if (n <= 0)
    return 0;
  if (n == 1)
    return 1;
  return f(n - 1) + f(n - 2);
}

int main()
{
  printf("f(8)=%d\n", f(8));
}
