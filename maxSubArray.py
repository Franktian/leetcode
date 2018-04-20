import sys

def maxSubArray(A):
    # REDO this
    curr = mxm = A[0]
    
    for num in A[1:]:
        curr = max(num, num + curr)
        mxm = max(mxm, curr)
    return mxm

def minCostClimbingStairs(cost):
    f1 = cost[0]
    f2 = cost[1]

    for n in cost[2:]:
        res = min(n + f1, n + f2)
        f1 = f2
        f2 = res

    return min(f1, f2)