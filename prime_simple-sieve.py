def seive(n):
    x=[True for i in range (n+1)]
    y=2
    num=0  
    while y*y<=n:
        if x[y]==True:
            for j in range(y*y,n+1,y):
                x[j]=False
                #print(j)
        y+=1
    for a in range(2,n+1):
        if x[a]==True:
            print(a)
seive(100000000)