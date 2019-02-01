/*
Each JEPG starts with a distnct header:
first 3 bytes: 0xff 0xd8 0xff
last byte: 0xe0, 0xe1, 0xe2, ..., 0xef
*/

#include <stdio.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Validate user input.
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Open memory card file.
    FILE *file = fopen(argv[1], "r");

    // If the forensic image cannot be opened for reading,
    if (file == NULL)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 2;
    }

    // Create a buffer.
    unsigned char buffer[BLOCK_SIZE];

    // Pointer to image file.
    FILE *img = NULL;

    // Counter for the number of JPEG files.
    int counter = 0;

    // Read file in one block of 512 bytes until the end of the file.
    while (fread(buffer, BLOCK_SIZE, 1, file) == 1)
    {
        // If JPEG is found,
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If there is an opened image file,
            if (counter > 0)
            {
                fclose(img);
            }

            // Make a new JPEG file named counter'th.jpg.
            char filename[8];
            sprintf(filename, "%03i.jpg", counter);

            // Open the image file.
            img = fopen(filename, "w");
            if (img == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
                return 3;
            }

            counter++;
        }

        // Write to image file.
        if (img != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, img);
        }
    }

    // Close files.
    fclose(img);
    fclose(file);

    return 0;
}
