#Q Program to count total number of negative elements in array
#Example
#Input: [5,-8,1,-9,-6]
#Output: count of negative elements: 3

'''
i =[int(x) for x in input("Input: ").split(' ')]
c =sum([1 for x in i if x<0])
print(c)
'''

#Q Program to find sum of all elements of an array
#Example
#Input: [5,8,1,9,6]
#Output: sum= 29
'''
i =sum([int(x) for x in input("Input: ").split(' ')])
print(i)
'''

#Q Find largest and smallest number in array?
#Example
#Input: [5,-2,9,-3,-10,8,15,0,9]
#Output: Max:15 Min:-10
'''
l=[int(x) for x in input("enter").split(' ')]
print("Max :",max(l))
print("Min :",min(l))
'''

#Q Program to print sum of all even numbers between 1 to n.
#Example
#Input: n = 10
#Output: 30 
#Explaination: 2+4+6+8+10
'''
n = int(input("Enter limit"))
s =sum([x for x in range(2,n+1) if x%2==0])
print(s)
'''

#Q Program to print sum of all odd numbers between 1 to n.
#Example
#Input: n = 10
#Output: 25
#Explaination: 1+3+5+7+9
'''
n = int(input("Enter limit"))
s =sum([x for x in range(1,n+1) if x%2!=0])
print(s)
'''

#Q Program to enter any number and calculate sum of its digits.
#Example 
#Input: 528 
#Ouput: 5+2+8 = 15
'''
num =int(input("Enter number"))
n,sum=num,0
while n>0:
    i=n%10
    sum+=i
    n=n//10
print(sum)

'''
#Q Program to enter any number and calculate multiplication of its digits.
#Example 
#Input: 528 
#Ouput: 5*2*8 = 80
'''
num =int(input("Enter number"))
n,mul=num,1
while n>0:
    i=n%10
    mul*=i
    n=n//10
print(mul)

'''

#Q Input a number and print the reverse of the num
#Example
#Input: 1367
#Output: 7631
'''
num=int(input("Enter number"))
n,rev=num,0
while n>0:
    i=n%10
    rev=(rev*10)+i
    n=n//10
print(rev)
'''

#Q Program to Calculate the Sum of first N Natural Numbers
#Example
#Input: N=10
#Output: Add numbers from 1 to 10 ---> 55
'''
n =int(input("enter num"))
print(sum([x for x in range(1,n+1)]))

'''

#Q Program to Find Factorial of a Number N
#Example
#Input: N = 5
#Output: Factorial = 1 x 2 x 3 x 4 x 5 = 120
'''
from functools import reduce

n= int(input("Enter num"))
print(reduce(lambda x,y:x*y,range(1,n+1)))
'''
#Q Program to Display first n Fibonacci numbers 
#Example
#Input: N = 8
#Output: 0,1,1,2,3,5,8,13
'''
n=int(input("Enter num"))
a,b=0,1
print(a)
for i in range(n):
    print(b)
    a,b=b,a+b
'''

#Q In an array 1 to 10 numbers are stored, one number is missing how do you find it?
#Example
#Input: [1,2,3,4,?,6,7,8,9,10]
#Output: 5

A=[1,2,3,4,6,7,8,9,10]
n=len(A)
s =(n+1)*(n+2)/2
d=s-sum(A)
print(d)

#Q Program to Check if a number is a Armstrong Number 
#(A number is a amstrong number if sum of cube of individual nos is equal to original no)
#Example
#Input: 153
#Output: Yes 
#Explaination: (1*1*1 + 5*5*5 + 3*3*3 = 153)
'''
n =int(input("Enter num"))
i,sum=n,0
while i>0:
    d=i%10
    sum+=(d**3)
    i=i//10
if sum==n:
    print("YES")
else :
    print("NO")
    
'''

#Q Program to Check Whether a Character is Vowel or Consonant
#Example
#Input: A
#Output: vowel
#Input: C
#Output: Consonant
'''
V='AEIOUaeiou'
ch =input("Enter")
if ch in V:
    print("Vowel")
else:
    print("Consonant")
'''

#Q Program to check whether a character is uppercase or lowercase alphabet.
#Example
#Input: 'a'
#Output: lowercase

ch =input("Enter char")
if ch.islower():
    print("Lower case")
elif ch.isupper():
    print("Upper case")
else:
    print("Wrong choice")































