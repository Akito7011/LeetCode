def plus_one(array):
    lent=len(array)
    digit1=0
    i=0
    powr=lent-1
    while lent>0:
        print(array[i])
        digit1+=array[i]*(10**(lent-1))
        print("digit1= ",digit1)
        i+=1
        lent-=1
    digit1+=1
    list1=[]
    for i in str(digit1):
        list1.append(int(i))
    print(list1)
plus_one([4,3,2,1])
        