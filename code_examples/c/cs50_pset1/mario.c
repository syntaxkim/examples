#include <stdio.h>

int main(void)
{
    // Prompt user for height.
    int height;
    do
    {
        printf("Height: ");
        scanf("%i", &height);
    }
    while (height < 1 || 8 < height);
    
    for (int i = 0 ; i < height ; i++)
    {
        // Print spaces.
        for (int space = height - i - 1 ; space > 0 ; space--)
        {
            printf(" ");
        }
        // Print blocks.
        for (int j = 0 ; j <= i ; j++)
        {
            printf("#");
        }
        
        // gap
        printf("  ");
        
        for (int j = 0 ; j <= i ; j++)
        {
            printf("#");
        }
        
        // New line
        printf("\n");
    }
}
