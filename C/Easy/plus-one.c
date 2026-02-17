/**
    # NAME: plus-one
    # URL: https://leetcode.com/problems/plus-one/
    # STATUS: Not completed!
    # RUN: cc plus-one.c -o plus-one; ./plus-one
*/

#include <stdio.h>
#include <stdlib.h>

int *plusOne(int* digits, int digitsSize, int* returnSize)
{
    int *digits2 = malloc(sizeof(int *) * *returnSize);
    int i = 0;
    while (i < *returnSize)
    {
        if (i < *returnSize - 1)
            digits2[i] = digits[i];
        else
            digits2[i] = digits[i] + 1;
        i++;
    }
    return digits2;
}


int main(void)
{
    int digits[6] = {1, 2, 3, 4, 5, 6};
    int returnSize = 6;
    int *digits2 = plusOne(digits, 6, &returnSize);

    int i = 0;
    printf("Plus One (+1): [");
    while (i < returnSize)
    {
        printf("%d", digits2[i]);
        if (i < returnSize - 1)
            printf(", ");
        i++;
    }
    printf("]\n");
    return 0;
}
