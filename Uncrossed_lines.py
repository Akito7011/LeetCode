def uncrossed(nums1,nums2):
    count=0
    len1=len(nums1)
    len2=len(nums2)
    for i in range(len1):
        k=i
        print(k)
        for j in range(k,len2):
            if nums1[i]==nums2[j]:
                k+=1
                print('k ',k)
                count+=1
                break
            else:
                k=i
                continue
    print(count)
uncrossed(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2])
            