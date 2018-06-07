def threeSum(nums):
    nums.sort()
    res = set()
    
    for k in range(len(nums)):
        target = -nums[k]

        i = k + 1
        j = len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                res.add((nums[k], nums[i], nums[j]))
                i += 1
                j -= 1
            elif nums[i] + nums[j] > 0:
                j -= 1
            else:
                i += 1
    return map(list, res)

def solution(A, B):
    
    wins = 0
    for i in range(len(A)):
        card_a = A[i]
        card_b = B[i]
        if check_win(card_a, card_b):
            wins += 1
    return wins

def check_win(card_a, card_b):
    if card_a == 'A':
        return card_b != card_a
    if card_a == 'K':
        return card_b not in 'AK'
    if card_a == 'Q':
        return card_b not in 'AKQ'
    if card_a == 'J':
        return card_b not in 'AKQJ'
    if card_a == 'T':
        return card_b not in 'AKQJT'

    return card_a > card_b