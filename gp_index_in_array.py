'''
You are given an array and you need to find number of tripets of indices  such that the elements at those
indices are in geometric progression for a given common ratio  and .
'''
from collections import Counter

def countTriplets(arr,r):
    count=0
    r2=Counter()
    r3=Counter()
    for v in arr:

        if v in r3:         #if k in r3 indicates the triplet already completed,
                            # the count need be incremented
            count+=r3[v]
        if v in r2:         #if k in r2, it is the secound number of the triplet,
                            # your successor (third element k*r) need be added or incremented in the r3 dict
            r3[v*r]+=r2[v]
        r2[v*r]+=1          # else, k is the first element of the triplet, so,
                # your seccessor (secound element k*r) need be added or incremented in the r2 dict
                # because is a potencial triplet

    print(count)


if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)