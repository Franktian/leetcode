def rotate(nums, k):
    sd = []
    
    for i in range(k):
        sd.append(nums.pop())
        
    sd2 = []
    for i in range(len(sd)):
        sd2.append(sd.pop())
        
    nums = sd2 + nums
    print nums