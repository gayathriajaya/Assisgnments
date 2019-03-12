'''
The word google can be spelled in many different ways.
E.g. google, g00gle, g0oGle, g<>0gl3, googl3, GooGIe etc...
Because

g = G

o = O = 0 = () = [] = <>

l = L = I

e = E = 3

That's the problem here to solve.
'''
import re

if __name__ == '__main__':
    string = 'G[]oGL3'
    pat = re.compile(r'[gG](\[\]|o)o[gG][Ll][eE3]')
    matches = pat.findall(string)
    for m in matches:
        print(m)

