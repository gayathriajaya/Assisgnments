'''
Given an array containing weights of gifts, and an integer K representing maximum weight a box can contain
(All boxes are uniform). Each box carries at most 2 gifts at the same time, provided the sum of the weight of those
gifts is at most limit of box. The task is to find the minimum number of boxes required to carry all gifts.
Note: It is guaranteed each gift can be carried by a box.
'''


def calculate(weights,tolal_weight):
    weights.sort()
    i,ans=0,0
    j=len(weights)-1
    while i<=j:
        ans+=1
        if weights[i]+weights[j]<=tolal_weight:
            i+=1
        j-=1
    return ans

weights=[3, 5, 3, 4]
total_weight=6
print(calculate(weights,total_weight))
