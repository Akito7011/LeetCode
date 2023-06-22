def elemental(nums, ggs=0, num=0):
    if not nums:
        print(num)
    else:
        count = nums.count(nums[0])
        if count > ggs:
            ggs = count
            num = nums[0]
        return elemental(nums[1:], ggs, num)
elemental([3,2,3])