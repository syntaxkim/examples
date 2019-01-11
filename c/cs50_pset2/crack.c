/* brute-force search algorithm */

/*
Assume that each password
1. has been hashed with C’s DES-based (not MD5-based) crypt function.
2. is no longer than five (5) characters. Gasp!
3. is composed entirely of alphabetical characters (uppercase and/or lowercase).
*/

#define _XOPEN_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <string.h>

// Brute force algorithms
int main(int argc, char *argv[])
{
    // Validate command line arguments.
    if (argc != 2)
    {
        printf("Usage: ./crack hash\n");
        return 1;
    }
    
    // Get salt.
    char salt[3];
    strncpy(salt, argv[1], 2);
    salt[2] = '\0';
    
    // Intialize alphabets.
    char letters[53] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int n = strlen(letters);
    letters[52] = '\0';

    // Initialize a candidate.
    char pwd[5] = "\0\0\0\0\0";

    // Enumerate all candidates.
    for (int d = 0 ; d < n ; d++)
    {
        for (int c = 0 ; c < n ; c++)
        {
            for (int b = 0 ; b < n ; b++)
            {
                for (int a = 0 ; a < n ; a++)
                {
                    pwd[0] = letters[a];
                    if (strcmp(crypt(pwd, salt), argv[1]) == 0)
                    {
                        printf("%s\n", pwd);
                        return 0;
                    }
                }
                pwd[1] = letters[b];
            }
            pwd[2] = letters[c];
        }
        pwd[3] = letters[d];
    }

    // If no matched passwords.
    printf("Could not crack.\n");

    return 2;
}
