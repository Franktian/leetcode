class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        mon_i = True
        mon_d = True
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                mon_d = False
            if A[i] > A[i - 1]:
                mon_i = False
    
        return mon_i or mon_d
