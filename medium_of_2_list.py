def sort_mid(nums1,nums2):
        list3=sorted(nums1+nums2)
        med=0
        lent=len(list3)
        if lent%2==0:
            temp=int(lent/2)
            #print(temp)
            med=(list3[temp-1]+list3[temp])/2
        else:
            lent+=1
            med=(list3[int((lent/2))-1])
        print(med)
sort_mid(nums1 = [1,3], nums2 = [2])