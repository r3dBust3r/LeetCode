/**
    # NAME: valid-palindrome
    # URL: https://leetcode.com/problems/valid-palindrome/
    # ISSUE: AddressSanitizer
    # RUN: cc valid-palindrome.c -o valid-palindrome; ./valid-palindrome
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int count_letters(char *s)
{
    int c = 0;
    int i = 0;
    while (s[i])
    {
        if ((s[i] >= 'a' && s[i] <= 'z') ||
            (s[i] >= 'A' && s[i] <= 'Z'))
            c++;
        i++;
    }
    return c;
}

int isPalindrome(char* s)
{
    char *d = malloc(sizeof(char) * count_letters(s) + 1);

    int j = 0;
    int i = 0;
    while (s[i])
    {
        if (s[i] >= 'a' && s[i] <= 'z')
            d[j++] = s[i];

        if (s[i] >= 'A' && s[i] <= 'Z')
            d[j++] = s[i] + 32;

        i++;
    }
    d[j] = '\0';

    int length = strlen(d);
    i = 0;
    while (i <= length / 2)
    {
        if (d[i] != d[length - 1 - i])
            return (free(d), 0);
        i++;
    }
    return (free(d), 1);
}


int main(void)
{
    if (isPalindrome("A man, a plan, a canal: Panama"))
        printf("True\n");
    else
        printf("False\n");
    return 0;
}
