def isValid(s):
    st = []

    for c in s:
        if c == '{' or c == '(' or c == '[':
            st.append(c)
        else:
            if c == '}' and st[0] != '{':
                return False
            if c == ']' and st[0] != '[':
                return False
            if c == ')' and st[0] != '(':
                return False
            st.pop()
    return st is []
