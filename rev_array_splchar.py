'''
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’),
reverse the string in a way that special characters are not affected.
 '''


def rev_array(s):
    str = list(s)
    l = 0
    r = len(str) - 1
#looping from both sides
    while l < r:
        if not str[l].isalpha():   #when front loop ele is not alpha
            l = l + 1
        elif not str[r].isalpha():   #when back loop ele is not alpha
            r = r - 1
        else:                           #when both ele are alpha
            str[l],str[r] =str[r],str[l]
            l=l+1
            r=r-1

    return ''.join(str)



print(rev_array('a!!b,c(d"ef'))