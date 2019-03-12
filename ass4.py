
#Q check if a given number is prime or not? 	

num=int(input("Enter nmber "))
flag=0
for i in range(2,num):
    if num%i==0:flag=1
if flag==1:print("Not prime")
else:print("Prime")


#Q Find the position of an number in a unsorted array.

list=[int(x) for x in input("Enter list").split(' ')]
num=int(input("Enter num"))
if num in list:
    print(list.index(num))
else:print(num," not present in list")


#Q Find the position of an number in a sorted array.

list=[int(x) for x in input("Enter list").split(' ' )]
s_list =sorted(list)
print(s_list)
num=int(input("Enter number"))
start ,stop,mid =0,len(s_list)-1,len(s_list)//2
flag=0
while start<=stop:
    mid=(start+stop)//2
    if num==s_list[mid]:
        pos=mid
        flag=1
        break
    elif num<s_list[mid]:
        stop=mid
    else:
        start=mid+1
if flag==1:
    print("POS" ,pos)
else:print("Not found")


#Q Find the Nth Fibonacci number
#Example
#Input: 15
#Output: 610


num=int(input("Enter num"))
a,b=0,1
for r in range(2,num+1):
    a,b=b,a+b
print(b)


#Q Find the Factorial of a number

#Example
#Input: 6
#Output: 720

num=int(input("Ener number"))
mul=1
for i in range(1,num+1):
    mul=mul*i
print(mul)

#Q Find the missing number in a array of size n where numbers vary from 1 to n? 
#Input:
#n = 5
#[3,1,5,?,2]
#Output: 4


n=int(input("Number:"))
list=[int(x) for x in input("list:").split(' ')]
ext_sum=n*(n+1)/2
act_sum=sum(list)
print("Missing num: ",int(ext_sum-act_sum))



#Q Find the first repeating element in an array of integers?
#Input:  arr[] = {10, 5, 3, 4, 3, 5, 6}
#Output: 5 [5 is the first element that repeats]

list=[int(x) for x in input("list:").split(' ')]
flag=0
for i in list:
    if list.count(i)>1:
        flag=1
        break
if flag==0:print("No repeeating nos")
else:print(i ,"is 1st repeting number")


#Q If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

list=[x for x in range(1000) if x%3==0 or x%5==0]
print(sum(list))


#Q Find first 5 prime palindromes numbers
#Output: 101, 79197, 324423, etc

count=0
a=100
b=100000
for i in range(a,b):
    flag=0
    if str(i)==str(i)[::-1]:
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
        if flag==0:
            print(i)
            flag=0
            count+=1
    if count==5:break


#Q Input the coins denomination from the user and the amount. 
#Make a coin calculator which finds out the least number of coins 
#required to compute an amount of money.

#Example
#Input:
#coins = [1,2,3,4,5]
#amount: 24
#24 = (4 X Rs. 5) + (1 X Rs. 3) + (0 X Rs. 2) + (1 X Rs. 1)

#Output:
#4 1 0 1


x=int(input("Enter the amount"))
den =[int(x) for x in input("Enter coins").split(' ')]
den.sort(reverse=True)
print(den)
num,sum=x,0
den_dict={}

while num!=0:
    for i in den:
        if num//i>=1:
            den_dict[i]=num//i
            num=num%i


print(den_dict)







