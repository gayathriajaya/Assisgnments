#Program to enter length and breadth of a rectangle and find its area & perimeter. 
#Example
#Input: len = 5, breadth = 3
#Output: Area = 15, Perimeter = 16
'''
length =int(input("Enter length"))
breadth=int(input("Enter breadth"))
p=(length+breadth)*2
ar=length*breadth

print("Area: ",ar," Perimeter :",p)


'''

#Q Program to enter radius of a circle and find its diameter, circumference and area.
#Example
#Input: radius = 7
#Output: Diameter = 14, circumference = 88, area = 154
'''
pi=22/7
radius=int(input("Enter radius"))
d=2*radius
c=2*pi*radius
ar=pi*(radius**2)
print("Diameter :",d," Circumference: ",c," Area: ",ar)

'''
#Q Program to enter base and height of a triangle and find its area.
#Example
#Input: b = 10, h = 20
#Output: Area = 100
'''
b=int(input("b="))
h=int(input("h="))
ar=(b*h)/2
print("Area: ",ar)
'''
#Q Program to enter temperature in °Celsius and convert it into °Fahrenheit.
#Example
#Input: 100
#Output: 212
'''
cel =int(input("Input : "))
f =(cel*9/5)+32
print("Output: ",f)
'''
#Q Program to enter marks of five subjects and calculate total, average and percentage.
#Example
#Input: 80,60,90,70,80
#Output: 76%
mark =[int(x) for x in input("Input: ").split(' ')]
total=sum(mark)
avg=total/len(mark)
percentage=total/(len(mark)*100) *100
print("Total: ",total," Average: ",avg,"Percentage: ",percentage,"%")



#Program to enter P, T, R and calculate Simple Interest.
#Example
#Input: Principle = 1200,  time: 2, rate: 5.4
#Output: SI = 129.60
'''
p=int(input("Principle: "))
t=int(input("time: "))
r=float(input("rate :"))
si=p*t*r/100
print("SI :",si)
'''

#Q Program to find maximum between three numbers.
#Example
#Input: a = 2, b = 3, c =1
#Output: b is maximum
'''
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
max=a
if b>max:
    max=b
if c>max:
    max=c
print(max," is max")
'''

#Q Program to check whether a number is negative, positive or zero.
#Example
#Input: -7
#Output: Negative Number
'''
num=int(input("Enter number"))
if num<0:
    print("Negative number")
elif num>0:
    print("Positive number")
else:
    print("Zero")
'''

#Q Program to Check Whether a Number is Prime or Not
#Example
#Input: 17
#Output: Prime Number
'''
num=int(input("Enter number: "))
flag=0
for i in range(2,num):
    if num%i==0:
        print("Not prime")
        flag=1
        break

if flag==0:
    print("Prime")
'''

#Q Program to Check Whether a Number is Even or Odd
#Example
#Input: 12
#Output: even
'''
num=int(input("Enter number: "))
if num==1:
    print("NOT EVEN NOT ODD")
elif num%2==0:
    print("Even")
else:
    print("odd")
'''

#Q Program to check whether a number is divisible by both 3 and 5 or not.
#Example
#Input: 15
#Output: Yes
'''
num=int(input("Enter number: "))
if num%3==0 and num%5==0:
    print("Yes")
else:
    print("No")
    
'''






