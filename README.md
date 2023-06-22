Translate_clip is a script I made to improve my productivity when translating text from Spanish to English or vice versa, by default sending the translated text to the clipboard ready to paste it wherever you need it, all from terminal.

 ##### I want to emphasize that I am running this little script in WSL version 1.2.5.0
 #
 #
## Installation
For the script to work you need a terminal tool called :
[translate-shell]( https://github.com/soimort/translate-shell )
```sh
sudo apt-get install translate-shell
```
and the terminal tool called xclip:
[xclip](https://github.com/astrand/xclip) 

```sh
sudo apt install xclip 
```

Now having everything ready, you just need to add the script to your path and choose the alias you want, in my case I use the following:
```sh
clip <text-to-translate> 
``` 




 
