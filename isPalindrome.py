def isPalindrome(x):
    if x < 0:
        return False

    nums = []
    while x > 0:
        nums.append(x % 10)
        x /= 10
    
    for i in range(len(nums) / 2):
        if nums[i] != nums[len(nums) - i - 1]:
            return False

    return True
