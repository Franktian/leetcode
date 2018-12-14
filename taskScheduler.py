class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        counts = [0] * 26
        
        for t in tasks:
            counts[ord(t) - ord('A')] += 1

        max_count = max(counts)
        num_max_count = 0
        
        for c in counts:
            if c == max_count:
                num_max_count += 1

        res = (max_count - 1) * (n + 1) + num_max_count

        return max(len(tasks), res)
