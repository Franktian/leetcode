def hammingDistance(x, y):
    # ^ xor, bit operation
    # TODO: practice base n conversion
    return bin(x ^ y).count(1)
