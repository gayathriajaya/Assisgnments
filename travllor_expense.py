

def trvel_exp(inputseq):
    if sum(inputseq)>=0:
        return 0
    elif sum(inputseq) <0:
        return -sum(inputseq)


i=[5,3,-10]
print(trvel_exp(i))