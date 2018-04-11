def plusOne(digits):
    carry = 0
    for i in reversed(range(len(digits))):
        if i == len(digits) - 1:
            s = digits[i] + 1
        else:
            s = digits[i] + carry
        if s == 10:
            carry = 1
        else:
            carry = 0
        digits[i] = s % 10
    
    if carry:
        return [carry] + digits
    return digits