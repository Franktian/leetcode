def calPoints(self, ops):
    """
    :type ops: List[str]
    :rtype: int
    """

    valid_scores = []
    s = 0

    for o in ops:
        if o == '+':
            score = valid_scores[-1] + valid_scores[-2]
            valid_scores.append(score)
            s += score
        elif o == 'D':
            score = valid_scores[-1] * 2
            valid_scores.append(score)
            s += score
        elif o == 'C':
            score = valid_scores.pop()
            s -= score
        else:
            valid_scores.append(int(o))
            s += int(o)
    return s
