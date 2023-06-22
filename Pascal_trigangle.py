def pascal(rows):
    temp=[]
    for i in range (rows):
        if len(temp)==0:
            temp.append([1])
        else:
            if len(temp)==1:
                temp.append([1,1])
            else:
                temp2=[1]
                lent=len(temp[-1])
                if lent%2!=0:
                    for i in range(lent-1):
                        if temp[-1][i]!=temp[-1][-1]:
                            x=temp[-1][i]+temp[-1][i+1]
                            print('val of ii=',i)
                            temp2.append(x)
                            print(x)
                        else:
                            temp2.append(1)
                    #print(temp2)
                    temp.append(temp2)
                elif lent%2==0:
                    for i in range(0,int(lent/2)+1):
                        if temp[-1][i]!=temp[-1][-1]:
                            print('val of i=',i)
                            x=temp[-1][i]+temp[-1][i+1]
                            temp2.append(x)
                            print(x)
                        else:
                            temp2.append(1)
                    #temp2.append(1)
                    print(temp2)
                    temp.append(temp2)
                        
                
    print(temp)
pascal(5)