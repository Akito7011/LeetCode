def merger(nums1,nums2,n):
    while 0 in nums1:
        nums1.remove(0)
    nums1+=nums2
    nums1=sorted(nums1)
    print(nums1)
merger(nums1 = [1,2,3,0,0,0],nums2 = [2,5,6], n = 3)