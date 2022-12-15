import random
def binary(s):
    k=int(s,16)
    m="{0:032b}".format(k)
    return m
def logic(s):
    fh=open('{}.trace'.format(s),'r')
    binar=[]
    for i in fh:
        binar.append(binary(i[4:13]))
    fh.close()
    cache={}
    hit=0
    p=0
    for i in binar:
        tag=i[0:14]
        index=i[14:30]
        offset=i[30:32] 
        if index in cache.keys():
            k=0
            for i in cache[index]:
                if (i[0]==tag):
                    hit+=1
                    p=random.randint(0,3)
                    i[1]=p
                    k+=1
                    break
            if k==0:
                if ([None,None] in cache[index]):
                    ind=cache[index].index([None,None])
                    cache[index][ind]=[tag,p]
                    p+=1
                else:
                    p=0
                    w=cache[index]
                    # m=min(w[0][1],w[1][1],w[2][1],w[3][1])
                    p=random.randint(0,3)
                    m=w[p][1]
                    for i in cache[index]:
                        if i[1]==m:
                            i[0]=tag
                            i[1]=p
                            break
        else:
            cache[index]=[[tag,p],[None,None],[None,None],[None,None]]

    c=len(binar)
    print("No.of Instructions-->",c)
    print("Hits are-->" ,hit)
    print("Misses are-->",c-hit)
    print("Hitrate is (in %)-->", round((hit/c)*100,4))
traces=["gcc", "gzip", "mcf", "swim", "twolf"]
for i in traces:
    print(i,"trace input")
    logic(i)
    print("----------------------------------")
# print(miss)