#include <stdio.h>

int calc_power(int base, int exponent)
{
    int result = 1;
    int counter = 0;
    while (counter < exponent)
    {
        result *= base;
        counter++;
    }
    return result;
}

int main()
{
    int output = calc_power(2, 3);
    printf("The answer is: %d\n", output);
    return 0;
}
