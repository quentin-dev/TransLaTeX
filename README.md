# TransLaTeX
A couple of python scripts that facilitate the translation of LaTeX content

**How to use TransLaTeX :** 
1. Paste all the important latex code in a file *Protip* : Try to exclude the front page and the appendix, and another part of your code with only LaTeX code
2. Run *translatex-fix.py filename*
3. Run all the "#-txt.txt" (where # is a number ) files through Google Translate & paste results into files called "#-en.txt"
  * **MAKE SURE YOU PROOFREAD THE TRANSLATION**
4. Run *translatex-reassembly.py max+1* 
5. Paste the contents of out.txt where it needs to go in your .tex file

*Have fun !*
