// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents number of buckets in a hash table
#define N 26

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Represents a hash table
node *hashtable[N];

// Hashes word to a number between 0 and 25, inclusive, based on its first letter
unsigned int hash(const char *word)
{
    return tolower(word[0]) - 'a';
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // Initialize hash table
    for (int i = 0; i < N; i++)
    {
        hashtable[i] = NULL;
    }

    // Open dictionary
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        unload();
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Insert words into hash table
    while (fscanf(file, "%s", word) != EOF)
    {
        // Allocate memory for a node. (heap)
        node *n = malloc(sizeof(node));
        n->next = NULL;

        // If no memory left,
        if (n == NULL)
        {
            unload();
            return false;
        }

        // Add the word to the newly created node.
        strcpy(n->word, word);

        // Hash the word to get an index.
        int i = hash(n->word);
        if (i < 0 || 25 < i)
        {
            unload();
            return false;
        }

        // If there's a list,
        if (hashtable[i] != NULL)
        {
            // Insert the node to the very first of a linked list.
            n->next = hashtable[i];
        }

        hashtable[i] = n;
    }

    // Close dictionary
    fclose(file);

    // Test print
    // for (int i = 0; i < N; i++)
    // {
    //     for (node *ptr = hashtable[i] ; ptr != NULL ; ptr = ptr->next)
    //     {
    //         printf("%s is loaded on hastable[%i]\n", ptr->word, i);
    //     }
    // }

    // Indicate success
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    unsigned int count = 0;
    // Traverse all buekcts.
    for (int i = 0 ; i < 26 ; i++)
    {
        // Traverse all nodes in a bucket.
        for (node *ptr = hashtable[i] ; ptr != NULL ; ptr = ptr->next)
        {
            count++;
        }
    }

    if (0 < count)
    {
        // dictionaries/large contains 143,091 words.
        return count;
    }

    return 0;
}

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // Get index.
    int i = hash(word);

    // Declare a pointer (cursor) that points to the same node that head pointer points to.
    node *cursor = hashtable[i];

    // Traverse linked list in the bucket.
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // From hashtable[0] to hashtable[N],
    for (int i = 0 ; i < N ; i++)
    {
        // Declare a pointer(cursor) to hashtable[i], the first node.
        node *cursor = hashtable[i];
        // Free memory until the end of the a linked list.
        while (cursor != NULL)
        {
            // Save the current node's location,
            node *tmp = cursor;
            // Move the cursor to the next node,
            cursor = cursor->next;
            // Free the current node.
            free(tmp);
        }
    }

    return true;
}
