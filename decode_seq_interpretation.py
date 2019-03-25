'''
Count Possible Decodings of a given Digit Sequence
Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given
 digit sequence
 Input:  digits[] = "121"
Output: 3
// The possible decodings are "ABA", "AU", "LA"

'''

def decode(digit,n):
    count=[0]*(n+1)
    count[0],count[1]=1,1

    for i in range(2,n+1):
        count[i]=0

        # If the last digit is not 0, then last
        # digit must add to the number of words
        if digit[i-1]>0:
            count[i]=count[i-1]

        # If second last digit is smaller than 2
        # and last digit is smaller than 7, then
        # last two digits form a valid character
        if digit[i-2] in [1,2] and digit[i-1]<=7:
            count[i]+=count[i-2]
    return count[n]

if __name__ == '__main__':
    arr=[1,2,3,4]
    print(decode(arr,len(arr)))