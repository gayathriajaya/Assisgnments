'''
Given an array of distinct integers and a sum value.
 Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).
'''

def count_pal_parti(arr,sum):
    arr.sort()
    n=len(arr)
    count=0
    for i in range(0,n-2):
        j=i+1
        k=n-1
        while j<k:
            if arr[i]+arr[k]+arr[j] >=sum:
                k=k-1
            else:
                count =count +(k-j)     #For current i and j, there  can be total k-j third elements.
                j=j+1

        return count

if __name__ == '__main__':
    arr = [5, 1, 3, 4, 7]
    sum = 12
    print(count_pal_parti(arr,sum))