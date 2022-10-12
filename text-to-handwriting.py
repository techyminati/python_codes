#!/usr/bin/env python3
#pip install pywhatkit
import pywhatkit as pykit

# Enter the Text to convert as Handwriting!!
text=input("Enter the text to convert")

# File to Save The Image 
pykit.text_to_handwriting (text, 'output.png', rgb=[125, 0, 250])

print ("The Image will Be Saved In Python Folder with Name 'output' :)")
