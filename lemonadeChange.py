class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        change = {
            5: 0,
            10: 0
        }
        
        for b in bills:
            if b == 5:
                change[5] += 1
            elif b == 10:
                if change[5] >= 1:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            elif b == 20:
                # Notice here always keep more 5 bills for optimal solution
                if change[5] >= 1 and change[10] >= 1:
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
        return True