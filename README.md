# Bad Apple in Source Academy
##### Using runes library in NUS CS1101S

https://share.sourceacademy.nus.edu.sg/adpple (Set to Source 4)

## What?
It creates an animated rune in Source Academy that plays the first 30s of Bad Apple at 10fps

[![Watch the video](https://img.youtube.com/vi/TYlJTw7pt7k/maxresdefault.jpg)](https://youtu.be/TYlJTw7pt7k)

## Why?
Runes provides the ability to stack images side by side each other, including full squares.
You know what else is full squares side by side each other, that's right pixels.

First thing that came to mind once I realised the possibility of a black and white display was Bad Apple. 
It seemed fun and so I made it.

## How?
Video reference: https://www.youtube.com/watch?v=9lNZ_Rnr7Jc
Frame extractor tool used: https://frame-extractor.com/

Process:
1. Used frame extractor tool to get 300 frames, 100ms apart from the first 30s of the video
2. Used python, Pillow library, to go through every image, crop it, resize it to 20x20 then read the pixel values
3. Using these pixel values, create a string in the format of an array that source academy can read 
(Needed to encode them into integers of 20 bits, so Source academy can handle it)
4. Paste array into Source Academy
5. Use stack_frac and beside_frac to create a grid of black and white squares given a matrix of 0s and 1s
6. Decode the data in the array and generate a frame
7. Pass the function to generate the frames into the built-in animate_rune function
