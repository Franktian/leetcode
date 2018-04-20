def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in nums:
        current_sum += i
        print current_sum
