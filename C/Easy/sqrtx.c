/**
    # NAME: sqrtx
    # URL: https://leetcode.com/problems/sqrtx/
    # RUN: cc sqrtx.c -o sqrtx; ./sqrtx
*/

#include <stdio.h>

int mySqrt(int x)
{
    int i = 0;
    while (i * i < x)
        i++;
    return i * i == x ? i : i - 1;
}

int main(void)
{
    int n = 21474800;
    printf("sqrt(%d): %d\n", n, mySqrt(n));
    return 0;
}
