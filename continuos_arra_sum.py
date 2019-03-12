


def con_sum_arr(inputSeq,targetSum):
    count=0
    for i in range(len(inputSeq)):
        for j in range(i, len(inputSeq)):
            if sum(inputSeq[i:j + 1]) == targetSum:
                count += 1
                break
            elif sum(inputSeq[i:j + 1]) > targetSum:
                break

    print(count)
'''
    for i,a in enumerate(arr):
        sum=a
        if a==k:
            count+=1
        elif a<k:
            for j in range(i+1,len(arr)):
                sum=sum+arr[j]
                if sum ==k:
                    count+=1
                    break
                elif sum<k:
                    continue
                else:
                    break
    print(count)
'''

arr=[6,2,4,1,5]
k=6
con_sum_arr(arr,k)