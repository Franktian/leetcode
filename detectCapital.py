def detectCapitalUse(word):
    num_lowers = 0
    num_uppers = 0
    for w in word:
        if w.isupper():
            num_uppers += 1
        else:
            num_lowers += 1
    
    if num_uppers == len(word):
        return True
    if num_lowers == len(word):
        return True
    if num_uppers == 1 and word[0].isupper():
        return True
    
    return False