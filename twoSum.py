def twoSum(nums, target):
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            print("{}, {}".format(nums[i], nums[j]))
            if (nums[i] + nums[j]) == target:
                return [i, j]
            
def twoSumHash(nums, target):
    dic = {}
    for i in range(0, len(nums)):
        comp = target - nums[i]
        ind = dic.get(comp)
        if ind != None:
            return [ind, i]
        dic[nums[i]] = i
