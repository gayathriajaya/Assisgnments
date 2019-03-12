'''

We define a word as a non-empty maximum sequence of characters that can contain only lowercase letters, uppercase
letters, digits and underscores '_' (ASCII value 95). Maximum sequence means that the word has to be immediately
preceeded by a character not allowed to occur in a word or by the left boundary of the sentence, and it has to be
immediately followed by a character not allowed to occur in a word or by the right boundary of the sentence.

Given  sentences and  words, for each of these words, find the number of its occurences in all the  sentences.

Input Format

In the first line there is a single integer . Each of the next  lines contains a single sentence. After that, in the
next line, there is a single integer  denoting the number of words. In the -th of the next  lines, there is a single
word denoting the -th word for which, you have to find the number of its occurences in the sentences.

Constraints



Output format

For every word, print the number of occurrences of the word in all the N sentences listed.
Hint :
deleting all the '_'s..
:: foo_bar --> foobar

2) putting '*' in first and last position..
:: foo foo foo -> *foo foo foo*

'''
import re

if __name__ == '__main__':
    n=int(input())
    s='\n'.join(['*'+input().strip().replace('_','')+'*' for  _ in range(n)])
    for _ in range(int(input())):
        wd=input().strip()
        reg = r'(?<=[\W])'+wd+'(?=[\W])'
        m=re.findall(reg,s)
        print(len(m))
