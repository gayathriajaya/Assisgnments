
if __name__ == '__main__':

    n=int(input())
    s=[int(x) for x in input().split()]
    absent=[x for x in range(1,n+1) if x not in s]
    print(' '.join(str(x) for x in absent))
