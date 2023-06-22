def rkdr(array,val):
        x=0
        lent=len(array)
        for i in array:
            if i==val:
                while array.count(i)>0:
                    array.remove(val)
            else:
                continue
        print(lent)
        print(array)
    #return x

rkdr([0,1,2,2,3,0,4,2],2)