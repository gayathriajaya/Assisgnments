import sys

def arrange(n,s):
    word=list(s)
    print(word)
    num=n
    mid=n//2

    count=0
    done=0
    for i,j in enumerate(word[:mid]):

        if j == word[num-1-i]:
            done= num -1-i

        elif j in word[mid:num-done]:
            ind= word[num-done :mid:-1].index(j)
            count =count+ind
            done=done-1- ind

        else :
            count=count+2
            done = done-1

    print(count)


def ispalin(s,st,end):
    while st <end:
        if s[st]!=s[end] :

            return False
        st=st+1
        end=end-1

    return True

def find_min_pal(s,n):
    for i in range(n-1,-1,-1):

        if ispalin(s,0,i):
            return n-i-1

def palindrm_count(s,st,end):

    if st>end :return sys.maxsize
    if st ==end :return 0
    if st == end-1 :
        return 0 if s[st]==s[end] else 1
    if s[st] == s[end]:

        return palindrm_count(s,st+1,end-1)
    else:
        return min(palindrm_count(s, st, end - 1), palindrm_count(s, st + 1, end))+1



if __name__ == '__main__':
    n=int(input())
    s=input()
    word=list(s)
    print(palindrm_count(word,0,n-1))