class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        result = []
        letters = []
        digits = []

        # Split and determine log type
        for l in logs:
            log = l.split()
            identifier = log[0]

            if log[1].isdigit():
                digits.append(l)
            else:
                letters.append(l.split(' ', 1))

        # Sort letter log by words & identifier
        letters = sorted(letters, key = lambda x: (x[1], x[0]))

        # Generate results
        for l in letters:
            result.append(' '.join(l))
        for d in digits:
            result.append(d)

        return result
