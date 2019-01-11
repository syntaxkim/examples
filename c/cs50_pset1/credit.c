/* luhn algorithm */

#include <stdio.h>

int main(void)
{
    // Prompt user for card number.
    long long number;
    do
    {
        printf("Number: ");
        scanf("%lli", &number);
    }
    while (number < 0);

    // Get first two digits.
    long long firsts = number;
    while (firsts >= 100)
    {
        firsts /= 10;
    }

    // Get first digit.
    long long first = number;
    while (first >= 10)
    {
        first /= 10;
    }

    // Count the length of a number.
    int length = 0;
    long long number_copy = number;
    while (number_copy != 0)
    {
        number_copy /= 10;
        length++;
    }

    // Checksum
    int sum = 0;
    int digitx2, digit;
    for (long long m = 10, n = 1 ; n < number ; m *= 100, n *= 100)
    {
        digit = (( number / n) % 10);
        digitx2 = ((number / m) % 10) * 2;
        sum += (digitx2 / 10) + (digitx2 % 10) + digit;
    }

    if (sum % 10 != 0)
    {
        printf("INVALID\n");
    }
    else if (first == 4 && (length == 13 || length == 16))
    {
        printf("VISA\n");
    }
    else if ((firsts == 34 || firsts == 37) && length == 15)
    {
        printf("AMEX\n");
    }
    else if ((50 < firsts && firsts < 56) && length == 16)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }

}