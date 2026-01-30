def SubSum(nums, k):
    samp = 0
    n = len(nums)

    for i in range(n):
        sumval = 0
        for j in range(i, n):
            sumval += nums[j]
            if sumval == k:
                samp += 1

    return samp


nums=[1,1,1,1]
k=2
print(SubSum(nums,k))
