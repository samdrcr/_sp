#include <stdio.h>

int power2(int n)
{
    int r = 1;
    for (int i = 0; i < n; i++)
    {
        r = r * 2;
    }
    return r;
}

int main()
{
    printf("power2(3) = %d\n", power2(3));
    return 0;
}
