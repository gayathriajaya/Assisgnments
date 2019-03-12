'''
Shyam is a travel guy. Being a coder, he can assume the world as a matrix. 

Shyam starts traveling from (0, 0). 
he takes one step in the x-direction and two steps in the y-direction alternatively. 

In short, he starts from (0, 0). he repeats following operations in sequence :
Take one step in x-direction.
Take two steps in y-direction.

Where will he be after M steps ? 
Input
First line contains T, number of test cases. Each test case contains M on a new line.

Output
For each test case output the coordinates for Shyam's final location.

Constraints
1 ≤ T ≤ 100
0 ≤ M ≤ 10^6
Example
Input:
5
0
1
2
3
4

Output:
0 0
1 0
1 1
1 2
2 2
'''

def find_pos(m):
    if m==0:
        pos=[0,0]
    else:
        
        a=m//3
        b=m%3
        if b!=0:
            pos=[(a+1),((2*a)+b-1)]
        else:
            pos=[a,(2*a)]
    return pos



n=int(input("Enter no of test cases 0<=T<=100"))
for i in range(n):
    m=int(input("Enter no of steps 0 ≤ M ≤ 10^6"))
    pos=find_pos(m)
    print("Pos:",pos)
    
    
