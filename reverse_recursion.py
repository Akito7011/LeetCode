
def reverse(x):
    if abs(x)< 0xffffffff:
        rev=0
        if x<0:
            x=x*-1
            while x>0:
                rev=rev*10+x%10
                x=x//10
                if rev< 0xffffffff:
                    return -rev
                else:
                    return 0
        else:
            while x>0:
                rev=rev*10+x%10
                x=x//10
                if rev< 0xffffffff:
                    return rev
                else:
                    return 0
    else:
        return 0
reverse(1563847412)