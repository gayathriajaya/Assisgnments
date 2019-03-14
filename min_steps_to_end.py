'''
Given an array of integers where each element represents the max number of steps that can be made forward from that
element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the
first element). If an element is 0, then we cannot move through that element.
'''
#dynamic programming

def minjump(arr,n):

    jump=[0 for _ in range(n)]

    if n==0 or arr[0]==0:
        return float('inf')

    for i in range(1,n):
        jump[i]=float('inf')
        for j in range(i):

            if (i<=j+arr[j] and jump[j]!=float('inf')):
                jump[i]=min(jump[i],jump[j]+1)

    return jump[n-1]

if __name__ == '__main__':
    arr=[1,3,4,1,0,2,2,4,1,9]
    print(minjump(arr,len(arr)))

