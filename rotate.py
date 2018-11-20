def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    k = k % l

    self.reverse(nums, 0, l - 1)
    self.reverse(nums, 0, k - 1)
    self.reverse(nums, k, l - 1)

def reverse(self, array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
