
import sys
#This module allows us to obtain the parameters from the script

import subprocess  
#This modulo allows us to execute commands in the shell

#In this variable we store the spanish text to translate
text = sys.argv[1]


# "trans" is the alias of the (Translate-shell) tool
# "trans -no-ansi -brief text-to-translate" is the command to get the simplified translation without any other information
#In this variables we store the output of the translation
english_trans_bytes = subprocess.check_output('trans -no-ansi -brief "{}"'.format(text), shell=True)
english_trans_text = english_trans_bytes.decode('utf-8')
 

#We print the result to verify that the translation is correct
print(english_trans_text)


