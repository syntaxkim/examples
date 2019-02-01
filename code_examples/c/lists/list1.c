// Implements a list of numbers using array with realloc.

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(void)
{
    int *numbers = NULL;
    int capacity = 0, size = 0;
    
    while (true)
    {
        int number;
        printf("Number: ");
        scanf("%i", &number);

        // Check for EOF
        if (number == 0)
        {
            break;
        }

        // If not enough memory to assign variable,
        if (size == capacity)
        {
            // Increase the size of an array by 1. (heap memory)
            numbers = realloc(numbers, sizeof(int) * (size + 1));
            capacity++;
        }
        numbers[size] = number;
        size++;
    }

    for (int i = 0 ; i < size ; i++)
    {
        printf("You inputtd %i\n", numbers[i]);
    }

    free(numbers);

    return 0;
}