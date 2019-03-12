'''
Number of subarrays having product less than K
'''

def num_subarray_prod(arr,k):
    count=0
    p=1
    for i,n in enumerate(arr):
        if n<=k:
            count=count+1
            p=n
            j=i+1
            while j<len(arr):
                if p*arr[j]<=k:
                    p=p*arr[j]
                    count=count+1
                    j=j+1
                else:break
    print(count)


a= [1, 9, 2, 8, 6, 4, 3]
k=100
num_subarray_prod(a,k)