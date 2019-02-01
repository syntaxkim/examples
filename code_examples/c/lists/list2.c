// Implements a list of numbers using a linked list.

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    // Memory for numbers
    node *numbers = NULL;

    // Prompt for numbsers (until EOF)
    while (true)
    {
        // Prompt for number
        int number;
        printf("Number: ");
        scanf("%i", &number);

        // Check for EOF
        if (number == 0)
        {
            break;
        }

        // Allocate space for number. (heap memory)
        node *n = malloc(sizeof(node));

        // If no memory left,
        if (!n) // (n == NULL)
        {
            return 1;
        }

        // Add number to list
        n->number = number; // (*n).number
        n->next = NULL;
        if (numbers)
        {
            for (node *ptr = numbers ; ptr != NULL ; ptr = ptr->next)
            {
                // If the current pointer(ptr)'s next field is the end of numbers node,
                if (!ptr->next) // (ptr->next == NULL)
                {
                    // Add number to the last node.
                    ptr->next = n;
                    break;
                }
            }
        }
        else // If the list is initially empty,
        {
            numbers = n;
        }
    }

    for (node *ptr = numbers ; ptr != NULL ; ptr = ptr->next)
    {
        printf("You inputtd %i\n", ptr->number);
    }

    // Free memory.
    node *ptr = numbers;
    while (ptr != NULL)
    {
        // Save the next node (Temporarily),
        node *next = ptr->next;
        // Free the current node,
        free(ptr);
        // Move the pointer to the next node.
        ptr = next;
    }

    return 0;
}