# Bad Apple in Source Academy
##### Using runes library in NUS CS1101S

https://share.sourceacademy.nus.edu.sg/adpple (Set to Source 4)

## What?
It creates an animated rune in Source Academy that plays the first 40s of Bad Apple

Initially, I planned to render an image made up of 20 x 20 square pixels but it became impractical beyond 30s at 10fps. 

After some research and thinking, I have used a quad tree to greatly boost performance, taking advantage of recursion and how the rune module works, significantly reducing space used the simple frames.

Using Quad trees and encoding them as strings, I managed to get a quad tree depth of 7, in other words 2**7=128 x 128 pixels worth of resolution

[![Watch the video (Normal)](https://img.youtube.com/vi/TLQjHRlrjBU/maxresdefault.jpg)](https://youtu.be/TLQjHRlrjBU)

[![Watch the video (Patchwork)](https://img.youtube.com/vi/jJIa40h_W4M/maxresdefault.jpg)](https://youtu.be/jJIa40h_W4M)

## Why?
Runes provides the ability to stack images side by side each other, including full squares.
You know what else is full squares side by side each other, that's right pixels.

First thing that came to mind once I realised the possibility of a black and white display was Bad Apple. 
It seemed fun and so I made it.

## How?
Video reference: https://www.youtube.com/watch?v=FtutLA63Cp8
Frame extractor tool used: https://frame-extractor.com/

Process:
1. Used frame extractor tool to get 800 frames, 50ms apart from the first 40s of the video
2. Used python, Pillow library, to go through every image, crop it, resize it to 128x128 then read the pixel values
3. Using these pixel values, recursively split the array into 4 subarrays everytime an array contains more than 1 unique value (Aka if not all white or not all black)
4. Generated a string for each frame through this recursive pattern with "0" representing black, "1" representing white and "2" representing splitting into 4 children
5. Paste an array of all the strings into Source Academy
6. Use parseData function which recursively iterates through the characters in the string and uses stack() and beside() to create the output rune
7. Use the built in animate_rune() with a generateFrame function that runs parseData on every index of the frame_data array

Additionally, I included a setting to better visualise and appreciate the quad tree, toggled through the patchwork boolean variable

By randomizing the colors of white and black slightly, the quad tree pattern becomes more visible