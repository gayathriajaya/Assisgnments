'''
Given  sentences consisting of one or more words separated by non-word characters, process q queries where each query
consists of a single string, s. To process each query, count the number of occurrences of q as a sub-word in all
sentences, then print the number of occurrences on a new line.
1
existing pessimist optimist this is
1
is
Ans 3
on;ly susbstring  not starting or end of word
'''

import re

n=int(input())
s='\n'.join(input() for _ in range(n))
t=int(input())


for _ in range(t):
    pat=r'\B'+input()+'\B'
    r=re.findall(pat,s)
    print(len(r))