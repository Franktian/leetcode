def longestMountain(self, A):
    """
    :type A: List[int]
    :rtype: int
    """
    max_length = 0
    N = len(A)
    
    start = 0
    while start < len(A):
        end = start

        if end + 1 < N and A[end] < A[end + 1]:
            while end + 1 < N and A[end] < A[end + 1]:
                end += 1
            
            if end + 1 < N and A[end] > A[end + 1]:
                while end + 1 < N and A[end] > A[end + 1]:
                    end += 1
                max_length = max(max_length, end - start + 1)

        start = max(end, start + 1)
    
    return max_length
