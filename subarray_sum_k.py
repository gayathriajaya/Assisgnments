import itertools
#NUMBER OF WAYS OF SUBARRAY SUM IS K
a=[1, 11, 2, 3, 15]
k=3
b=[10, 2, -2, -20, 10]
s=-10
r=sum([1 for i in range(1,len(b)) for seq in itertools.combinations(b,i) if sum(seq)==s])
print(r)

