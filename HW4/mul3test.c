#include <stdio.h>

int mul3(int a, int b, int c)
{
    return a * b * c;
}
int main()
{
    printf("mul3(3,2,5)=%d\n", mul3(3, 2, 5));
    return 0;
}