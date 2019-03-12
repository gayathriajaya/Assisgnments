'''
There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array obtained
after merging the above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n)).
'''


def median_equal(ar1,ar2,n):
    i,j=0,0
    m1,m2=-1,-1

    count=0
    while count<=n:
        count+=1

        if i==n:    # Below is to handle case where all elements of ar1[] are smaller than smallest(or first) element of ar2[]
            m1=m2
            m2=ar2[0]
            break
        if j==n:
            m1=m2
            m2=ar1[0]

        if ar1[i]<ar2[j]:
            m1=m2
            m2=ar1[i]
            i+=1
        else:
            m1=m2
            m2=ar2[j]
            j+=1

    return (m1+m2)/2


ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
    print("Median is ",median_equal(ar1, ar2, n1))
else:
    print("Doesn't work for arrays of unequal size")