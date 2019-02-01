# Questions

## What's `stdint.h`?

A header file in the C standard library to allow programmers to write more portable code by providing a set of typedefs that specify exact-width integer types, together with the defined minimum and maximum allowable values for each type, using macros.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

To conveniently define structures following the file formats of standard BMP.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

BYTE: 1, DWORD: 4, LONG: 4, WORD, 2

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

ASCII: BM, decimal: 6677, hexadecimal: 0x424d

## What's the difference between `bfSize` and `biSize`?

`bfSize` is the size of the whole BMP file.
`biSize` is the size of the BITMAPINFOHEADER only. It is 40 bytes.

## What does it mean if `biHeight` is negative?

The bitmap is a top-down DIB and its origin is the upper-left corner.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount (determines the number of bits that define each pixel and the maximum number of colors in the bitmap.)

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

The file could not exist or be read by access denial.

## Why is the third argument to `fread` always `1` in our code? (For example, see lines 40, 44, and 75.)

Because the program is going to read the file by 1 element.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

(4 - (3 * 3) % 4) % 4 = 3

## What does `fseek` do?

`fseek` sets the file position of the stream to the given offset.
```
// skip over padding, if any
fseek(inptr, padding, SEEK_CUR);
```
Add padding bytes of offset to the current position of the file pointer.

## What is `SEEK_CUR`?

The current position of the file pointer.
