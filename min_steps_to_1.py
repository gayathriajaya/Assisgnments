'''
Given a number n, count minimum steps to minimize it to 1 according to the following criteria:

If n is divisible by 2 then we may reduce n to n/2.
If n is divisible by 3 then you may reduce n to n/3.
Decrement n by 1.
'''

def min_steps(n):
    if n==1:
        return 0
    dp =[0]*(n+1)
    for i in range(2,n+1):   #because 1 is the result starts with 2
        dp[i]=1+ dp[i-1]
        if i%2!=0:
            dp[i]=min(dp[i], 1 + dp[i//2])
        if i%3==0:
            dp[i] =min(dp[i], 1+dp[i//3])
    return dp[n]

if __name__ == '__main__':
    print(min_steps(10))
