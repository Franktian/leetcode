def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """

    res_str = ""
    MAX_INT = 2147483647
    MIN_INT = -2147483648

    for c in str:
        if len(res_str) == 0 and c == ' ':
            continue
        elif len(res_str) == 0 and (c == '-' or c == '+'):
            res_str += c
        elif c.isdigit():
            res_str += c
        elif len(res_str) > 0 and not c.isdigit():
            break
        elif len(res_str) == 0 and (not c.isdigit() or c != '-' or c != '+'):
            break
    if len(res_str) == 0:
        return 0
    if res_str == '-' or res_str == '+':
        return 0

    res = int(res_str)

    return max(MIN_INT, min(res, MAX_INT))
