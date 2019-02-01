/* vigenere algorithm */

#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    // Validate command line arguments.
    if (argc != 2)
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
    else
    {
        for (int i = 0, n = strlen(argv[1]) ; i < n ; i++)
        {
            if (isalpha(argv[1][i]) == 0)
            {
                printf("Usage: ./vigenere keyword\n");
                return 1;
            }
        }
    }

    // Get the plaintext from a user.
    char p[20];
    printf("plaintext: ");
    gets(p);

    // Encipher.
    char *c = malloc((strlen(p) + 1) * sizeof(char));
    for (int i = 0, j = 0, k = 0, n = strlen(p) ; i < n ; i++)
    {
        if (isupper(argv[1][j]))
        {
            k = argv[1][j] - 'A';
        }
        else if (islower(argv[1][j]))
        {
            k = argv[1][j] - 'a';
        }

        if (isupper(p[i]))
        {
            c[i] = 'A' + (((p[i] - 'A') + k) % 26);
            j++;
        }
        else if (islower(p[i]))
        {
            c[i] = 'a' + (((p[i] - 'a') + k) % 26);
            j++;
        }
        else
        {
            c[i] = p[i];
        }

        j %= strlen(argv[1]);
    }

    // Output ciphertext.
    printf("ciphertext: %s\n", c);

    free(c);

    return 0;
}
