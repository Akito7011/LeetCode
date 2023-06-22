class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        dir=0 
        top=0
        bottom=(len(matrix)-1)
        right=(len(matrix[0])-1)
        left=0
        l2=[]
        while top<=bottom and left<=right:
            if dir==0:
                for i in range(left,right+1):
                    l2.append(matrix[top][i])
                top+=1
            elif dir==1:
                for i in range(top,bottom+1):
                    l2.append(matrix[i][right])
                right-=1
            elif dir==2:
                for i in range(right,left-1,-1):
                    l2.append(matrix[bottom][i])
                bottom-=1
            elif dir==3:
                for i in range(bottom,top-1,-1):
                    l2.append(matrix[i][left])
                left+=1
            dir=(dir+1)%4
        return l2
            