'''
100 people are standing in a circle with gun in their hands.
    1 kills 2, 3 kills 4, 5 kills 6 and so on till we are
    left with only one person. Who will be the last person alive?
    Write code to implement this ##efficiently.## <-[ Python is not efficient]

'''

person=list(range(1,101))

while len(person)>1:
    print()
    for i,_ in enumerate(person):
        print(_,end=' ')
        del person[(i+1)% len(person)]

print(person)


import copy

person=list(range(1,101))
p=copy.deepcopy(person)


for i,v in enumerate(p):
    if i%2==0:
        p.append(v)
    else:
        person.remove(v)
        if len(person)==1:
            break


print(person[0])