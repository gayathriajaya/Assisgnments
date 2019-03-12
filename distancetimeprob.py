'''
Ram and Shyam are on security patrol.

They start from a checkpoint and go in opposite direction for greater coverage.
Ram starts with speed U metre/second and Shyam starts with speed V metre/second. 
They both have a walkie-talkie, operating for maximum distance of X metres. How long will they be able to communicate ?

Input
First line contains number of test cases.
Each test contains three integers U, V and X on a new line.


Output
For each test case output the required answer in seconds on the new line. 
Your answer will be considered correct if it has an absolute error less than 1e-6.


Constraints
1 ≤ T ≤ 1000
1 ≤ U, V ≤ 2 * 10^9
1 ≤ X ≤ 2000
 

Example
Input:
3
3 3 3
6 2 4
38 47 847

Output:
0.5000000000
0.5000000000
9.9647058824
'''





def calculatetime(u,v,x):
    time=x/(u+v)
    return time


n=int(input("Enter no of test cases"))
for i in range(n):
    
    u=int(input("Enter U"))
    v=int(input("Enter V"))
    x=int(input("Enter X"))
    print("Time taken :",calculatetime(u,v,x))
