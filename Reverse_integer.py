def reverse(x):
    if abs(x)<2**32 and abs(x)!=2**32-1:
        rev=0

        if x<0:
            x=x*-1
            while x>0:
                rev=rev*10+x%10
                x=x//10
            print(-rev)
        else:
            while x>0:
                rev=rev*10+x%10
                x=x//10
            print(rev)
            print('end')
            if rev<2**31 and rev!=2**31-1:
                return rev
            else:
                return 0
    else:
        return 0
    
reverse(1563847412)