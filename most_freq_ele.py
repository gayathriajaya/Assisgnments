#most freq ele in list using dict

def most_freq(l):
    d={}
    count,itm=0,''     #contains max count and that item
    for i in dict:
        d[i]=d.get(i,0)+1
        if d[i] > count:
            count,itm =d[i],i
    return i