'''
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
Before we go further, let us understand with few examples:

ab: Number of insertions required is 1 i.e. bab
aa: Number of insertions required is 0 i.e. aa
abcd: Number of insertions required is 3 i.e. dcbabcd
abcda: Number of insertions required is 2 i.e. adcbcda which is same as number of insertions in the substring bcd(Why?).
abcde: Number of insertions required is 4 i.e. edcbabcde
'''
import sys


# Recursive method
def find_min_ins(s, l, h):
    if l > h:
        return sys.maxsize
    if l == h:
        return 0
    if l == h - 1:
        return 0 if s[l] == s[h] else 1  # only 2 elements

    if s[l] == s[h]:
        return find_min_ins(s, l + 1, h - 1)  # same elements
    else:
        return min(find_min_ins(s, l, h - 1), find_min_ins(s, l + 1, h)) + 1

#Dynamic programming
def find_min_pal(s,n):
    table =[[0 for _ in range(n)]for _ in range(n)]

#gap is gap length of substring ie, ab,bc,cd,de for 1, abc,bcd,cde for 2 etc
    for gap in range(1,n):
        l=0
        for h in range(gap,n):
            if s[l]==s[h]:
                table[l][h]=table[l+1][h-1]
            else:
                table[l][h]=min(table[l+1][h],table[l][h-1])+1
            l+=1
    return table[0][n-1]



if __name__ == '__main__':
    sh = 'abcde'
    se='abca'
    print(find_min_ins(sh, 0, len(sh) - 1))
    print(find_min_pal(se,len(se)))   # ans : abcba ie 1
