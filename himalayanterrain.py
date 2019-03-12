'''
Q2 Himalayas Terrain
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap from rivers.


Input: arr[]   = {2, 0, 2}
Output: 2
Structure is like below
| |
|_|
We can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 0, 2, 0, 4}
Output: 10
Structure is like below
     |
|    |
|  | |
|__|_| 
We can trap "3*2 units" of water between 3 an 2,
"1 unit" on top of bar 2 and "3 units" between 2 
and 4.  See below diagram also.

Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
       | 
   |   || |
_|_||_||||||
Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2 



'''

arr1 =[2,0,2]
arr2 =[3,0,0,2,0,4]
arr3=[0,1,0,2,1,0,1,3,2,1,2,1]

arr= arr2


'''
arr = arr3
n = len(arr)

left = [0 for x in range(n)]
right = [0 for x in range(n)]

m = -1
i = 0
while i<n:
    if max(arr[i],m) >= m:
        m = max(arr[i],m)

    left[i] = m
    i+=1

print(left)




m = -1
i = n-1
while i>=0:
    if max(arr[i],m) >= m:
        m = max(arr[i],m)

    right[i] = m
    i-=1

print(right)


count = 0

i = 0
while i<n:
    left_max = left[i]
    right_max = right[i]
    min_value = min(left_max,right_max)
    diff = min_value - arr[i]
    count += diff

    i+=1

print("Amount of water stored:",count,"units")

method 2 :
'''
arr=arr3
count=sum( min(max(arr[:i+1]),max(arr[i:]))-arr[i] for i in range(len(arr)))
print("The no od units of water trapped is ",count)



















