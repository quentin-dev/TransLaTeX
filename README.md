# TransLateX
A couple of python scripts that facilitate the translation of LateX content

How to use Translatex : 
1) Paste all the important latex code in a file called "input.txt" 
1.5)Protip : Try to exclude the front page and the appendix, and anyother part of you code with only latex code
2) Run tranlatex-fix.py
3) Run all the "#-txt.txt" (where # is a number ) files through Google Translate & paste results into files called "#-en.txt"
4) Change the 7 on line 3 in reassemble.py to your max number + 1
5) Run translatex-reassembly.py
6) Paste the contents of out.txt where it need to go in your .tex file
Have fun !
