def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    results = [0] * n
    results[1] = 1
    
    for i in range(2, n):
        results[i] = results[i - 1] + results[i - 2]
    
    return results

def checkSum(A, T):
    left = right = 0
    s = 0
    
    while left < len(A):
        while s < T and right < len(A):
            s += A[right]
            right += 1
        
        if s == T:
            return True
        s -= A[left]
        left += 1

    return False


def buyStock(prices):
    minimum = prices[0]
    max_profit = 0
    
    for p in prices[1:]:
        minimum = min(minimum, p)
        max_profit = max(max_profit, p - minimum)
    
    return max_profit


def productExceptSelf(array):
    n = len(array)
    lefts = [1] * n
    rights = [1] * n
    
    for i in range(1, n):
        lefts[i] = lefts[i - 1] * array[i - 1]
        rights[n - i - 1] = rights[n - i] * array[n - i]
    
    print lefts
    print rights
    
    for i in range(n):
        lefts[i] *= rights[i]
    
    return lefts[i]


def checkConsecutive(array):
    maximum = max(array)
    minimum = min(array)
    
    if maximum - minimum + 1 == len(array):
        for i in range(len(array)):
            if array[i] < 0:
                j = -array[i] - minimum
            else:
                j = array[i] - minimum
            
            if array[j] > 0:
                array[j] *= -1
            else:
                return False
        return True
    return False


def isValid(s):
    st = []
    
    for c in s:
        print st
        if c == '(':
            st.append(c)
        elif not st or st.pop() != '(':
            return False

    return not st


if __name__ == '__main__':    
    print isValid('()')
    print isValid(')(')
