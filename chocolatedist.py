'''

'''
a=[]

def count_students(m,n,p,q):
    for i in range(m,n+1):
        for j in range(p,q+1):
            count(i,j,0)
    print(sum(a))

    #print(scount)

def count(i,j,scount):
    if i - j == 0:
        scount=scount+1
        a.append(scount)
    elif i< j:
        scount = scount + 1
        count(i,j-i,scount)
    else:
        scount = scount + 1
        count(i-j,j,scount)


if __name__ == '__main__':
    m,n =[int(x) for x in input().split(' ')]
    p,q=[int(x) for x in input().split(' ')]
    if m>=1 & q<=200:
        count_students(m,n,p,q)
    else:print("False input")