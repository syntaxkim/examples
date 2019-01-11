/* greedy algorithm */

#include <stdio.h>
#include <math.h>

int change(int cents);

int main(void)
{
    // Prompt user for owed change.
    float dollars;
    do
    {
        printf("Change owed: ");
        scanf("%f", &dollars);
    }
    while (0 > dollars);
    
    // Convert dollars to cents.
    int cents = round(dollars * 100);
    
    // Calculate the number of coins.
    int coins = change(cents);
        
    printf("%i\n", coins);
}

int change(int cents)
{
    int quarters = 0; // 25c
    int dimes = 0; // 10c
    int nickels = 0; // 5c
    int pennies = 0; // 1c

    quarters = cents / 25;
    dimes = (cents - (quarters * 25)) / 10;
    nickels = (cents - (dimes * 10) - (quarters * 25)) / 5;
    pennies = (cents - (nickels * 5) - (dimes * 10) - (quarters * 25)) / 1;
    
    return quarters + dimes + nickels + pennies;
}
