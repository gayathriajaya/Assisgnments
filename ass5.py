
'''
Q Find Two Missing Numbers
Given an array of n unique integers where each element 
in the array is in range [1, n]. The array has all 
distinct elements and size of array is (n-2). 
Hence Two numbers from the range are missing from this array. 
Find the two missing numbers.

Input: arr = [1, 3, 5, 6]
Output: 2 4
Explaination:


      
arr=[int(x) for x in input("Enter").strip().split(' ')]
arr1=[x for x in range(arr[0],arr[-1])]

print("Missing elements :", set(arr1)-set(arr))


Q Reverse an array in groups of given size

Input: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
Output: [3, 2, 1, 6, 5, 4, 9, 8, 7]
Explaination: Given an array, reverse every sub-array formed by 
consecutive k elements


arr=[int(x) for x in input("Enter").strip().split(' ')]
k=int(input("Enter k"))
i=0
while i<=(len(arr)-3):
    arr[i:k+i] =reversed(arr[i:k+i])
    i+=k
    
print(arr)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Q Find all triplets in a sorted array that forms Geometric Progression
Input: arr = [1, 2, 6, 10, 18, 54]
Output: 2 6 18 and 6 18 54
Explaination:


import math
arr=[int(x) for x in input("Enter").strip().split(' ')]

dis=[]
for i,x in enumerate(arr):
    for y in arr[i+1:]:
        if math.sqrt(x*y) in arr:
            print(x,y,int(math.sqrt(x*y)))



Q Find if array can be divided into two subarrays of equal sum
Input: arr = [6, 2, 3, 2, 1]
Output: true
Explaination: Given an array of integers, find if it’s possible
to remove exactly one integer from the array that divides the array into two subarrays with the same sum.



arr=[int(x) for x in input("Enter").strip().split(' ')]

for i in range(len(arr)):
    if sum(arr[:i])==sum(arr[i+1:]):
        print("True")
        break  
else:print("False")



Q Remove duplicates from an array of small primes
Input: arr = {3, 5, 7, 2, 2, 5, 7, 7};
Output: arr = {2, 3, 5, 7}
Explaination: Given an array of primes such that the range of primes
is small. Remove duplicates from the array.



arr=[3, 5, 7, 2, 2, 5, 7, 7]
print(set(arr))



Q Given an array A[], write a function that segregates even 
and odd numbers.
Input: {12, 34, 45, 9, 8, 90, 3}
Output: {12, 34, 8, 90, 45, 9, 3} 
Explaination: It should put all even numbers first, then odd numbers.


input =[12, 34, 45, 9, 8, 90, 3]
op_even=[]
op_odd=[]
#for x in input:
 #   op_even.append(x) if x%2==0 else op_odd.append(x)

[op_even.append(x) if x%2==0 else op_odd.append(x) for x in input]
op=op_even+op_odd
print(op)


Q Find a triplet that sum to a given value
Input: {12, 3, 4, 1, 6, 9} , sum =24
Output: True
Explaination:  find if there is a triplet in array whose sum is 
equal to the given value. If there is such a triplet present in 
array, then print the triplet and return true. Else return false


import itertools

inp={int(x) for x in input("Input :").strip().split(' ')}
s =int(input("Sum= "))
comb =set(itertools.combinations(inp,3))
print("true") if s in map(sum,comb) else print("False")


Q Given an array and a number x, find if there is a pair with 
product equal to x.
Input: arr = {10, 20, 9, 40}, x = 400;
Output: Yes
Explaination: 


import itertools
inp={int(x) for x in input("Input :").strip().split(' ')}
p =int(input("product= "))
print("True") if p in [x[0]*x[1] for x in set(itertools.combinations(inp,2))] else print("False")

Q Given an array of integers, and a number ‘sum’, find the number
 of pairs of integers in the array whose sum is equal to ‘sum’.
Input: arr = {1, 5, 7, -1}, sum = 6
Output: 2 (Pairs with sum 6 are (1, 5) and (7, -1))
Explaination:

import itertools
inp= [int(x) for x in input("Input :").strip().split(' ')]
s =int(input("sum: "))
d=[x for x in set(itertools.combinations(inp,2)) if x[0]+x[1]==s]

print(len(d),"Pairs with sum ",s,"are ",d)


Q Given heights of n towers and a value k. We need to either 
increase or decrease height of every tower by k (only once) 
where k > 0. The task is to minimize the difference between 
the heights of the longest and the shortest tower after modifications, 
and output this difference.

Input: arr = {1, 15, 10}, k = 6
Output: arr = {7, 9, 4}, Maximum difference is 5.
Explaination: We change 1 to 6, 15 to 9 and 10 to 4. Max diff is 5
(between 4 and 9). We cannot get a lowerdifference.

'''
import math
inp= [int(x) for x in input("Heights :").strip().split(' ')]
k =int(input("k: "))
op=[]
for i in range(len(inp)):
    if inp[i]<k:
        op.append(inp[i]+k)
        continue
    if i==0:
        d=abs(inp[0]-inp[1])
    else:
        d=abs(inp[i]-op[-1])
    op.append(inp[i]+k) if abs(d+k)<abs(d-k) else op.append(inp[i]-k)
    
print(op," Diff is ", max(op)-min(op))

















