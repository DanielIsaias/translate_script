#This is a test
#This is the command the you need to obtein the translate text 
#trans -no-ansi -brief  "hola mundo" (automaticamente lo manda a ingles) 

import subprocess  

#In this variable we store the spanish text to translate
text = "" 


#In this variable we store the output of the translation 
english_trans = subprocess.check_output("trans -no-ansi -brief "+ , shell=True)

