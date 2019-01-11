/* caeser algorithm */

#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    // Validate command line arguments.
    if (argc != 2)
    {
        printf("Usage: ./caesar key.\n");
        return 1;
    }
    else
    {
        for (int i = 0, n = strlen(argv[1]) ; i < n ; i++)
        {
            if (isalpha(argv[1][i]) != 0)
            {
                printf("Usage: ./caesar key.\n");
                return 2;
            }
        }
    }

    // Convert string to interger.
    int k = atoi(argv[1]);

    // Get the plaintext from a user.
    char p[20];
    printf("plaintext: ");
    gets(p);

    // Encipher.
    char *c = malloc((strlen(p) + 1) * sizeof(char));
    for (int i = 0, n = strlen(p) ; i < n ; i++)
    {
        if (isupper(p[i]))
        {
            c[i] = 'A' + (((p[i] - 'A') + k) % 26);
        }
        else if (islower(p[i]))
        {
            c[i] = 'a' + (((p[i] - 'a') + k) % 26);
        }
        else
        {
            c[i] = p[i];
        }
    }

    // Output ciphertext.
    printf("ciphertext: %s\n", c);

    free(c);

    return 0;
}
