'''
Q1

Megha is turning  years old! Therefore, she has  candles of various heights on her cake, 
and candle  has height . Because the taller candles tower over the shorter ones, 
Megha can only blow out the tallest candles.

Given the  for each individual candle, find and print the number of candles 
she can successfully blow out.

Input Format

The first line contains a single integer, , denoting the number of candles on the cake. 
The second line contains  space-separated integers, where each integer  describes the height of candle .

Constraints

Output Format
Print the number of candles Megha blows out on a new line.


Sample Input 0

4
3 2 1 3

Sample Output 0
2

Sample Input 0

10
3 2 4 1 2 5 1 4 6 9

Sample Output 0
2
'''
arr1 =[3,2, 1, 3]
arr2 = [3,2,4,1,2,5,1,4,6,9]

n =int(input("Enter no of candles"))
arr = [int(x) for x in input("Enter height ").strip().split(' ')]
count=0
max_vals=-1
for x in arr:
    if x>max_val:
        count+=1
        max_val =x
        
print(count)























