def spiral_matrix(n):
    dir=0
    top=0
    bottom=(n-1)
    right=(n-1)
    left=0
    sum=1
    temp=[[0 for j in range(n)] for i in range(n)]
    print(temp)
    while top<=bottom and left<=right:
        if dir==0:
            for i in range(left,right+1):
                temp[top][i]=sum
                sum+=1
            top+=1
        elif dir==1:
            for i in range(top,bottom+1):
                temp[i][right]=sum
                sum+=1
            right-=1
        elif dir==2:
            for i in range(right,left-1,-1):
                temp[bottom][i]=sum
                sum+=1
            bottom-=1
        elif dir==3:
            for i in range(bottom,top-1,-1):
                temp[i][left]=sum
                sum+=1
            left+=1
        dir=(dir+1)%4
    print(temp)
    return temp
    
                
    
    
    
spiral_matrix(3)