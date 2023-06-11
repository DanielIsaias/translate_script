#!/usr/bin/python3

import sys
#This module allows us to obtain the parameters from the script

import os 
#This module allows us to execute simple commands in the operating system

#In this variable we store the spanish text to translate
try:
    text = sys.argv[1]
except IndexError:
    print("Error, no igresaste ningun texto")
    exit() 

# "trans" is the alias of the (Translate-shell) tool
# "trans -no-ansi -brief text-to-translate" is the command to get the simplified translation without any other information


#Execute the command that will send the translated text to the clipboard
os.system('trans -no-auto -no-ansi -brief "{}" | xclip -selection clipboard'.format(text))


print("The text was copied to the clipboard. :)") 

