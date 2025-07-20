INTRODUCTION:

Hello! This is my very first actual programming project. I'm currently on Week 2 of CS50P (loops, lists and dicts), and decided to make something that uses that knowledge. A scytale was a tool used for cryptography. Wikipedia explains it with images (worth 1000 words!)
https://en.wikipedia.org/wiki/Scytale
~~This program (so far) only encrypts text, though I plan on adding a decryption function sometime in the future (in the works, just working on debugging)~~
Finally added. See scytaleimproved.py for it. I kept the old one up for posterity, though I could probably make it a release. I'm still learning my way around GitHub.

The first version processed the string through substrings. I chose an array of characters instead as that'd allow me to encrypt and decrypt with ease.

HOW TO USE:
This is a CLI program. Run it in Python. It'll ask you for the text to be encrypted, then it'll ask you the width of the scytale, and then return the encrypted text. Ez. 

POSSIBLE FUTURE ADDITIONS:
~~Splitting letters in strings as arrays would make it much easier both to encrypt and decrypt letters I found. Decryption algorithm would require strings to be configured differently (you can't use the "separate_words" thing for decryption), and working with lists is kind of inefficient. That could work.~~
Finally added! 

GUI with TKinter or PySimpleGUI for ease of use. Grid could be created based on length OR width instead of just width. Wrapping all 4 variables (string, width, length, grid) in a class as attributes and encryption/decryption as methods would make the main() function substantially easier to read for me personally. 

Rewriting the program with OOP instead of complete functionality. The length, width, grid and string are much better as attributes of a Scytale class. Not to mention I have an entire function just to initialize the variables (init_scytale) in lieu of defining self attributes and being done with it that way. In this regard, the only two user inputted variables (string and width) could be taken as input and the rest can be gleamed from the two as methods. 
