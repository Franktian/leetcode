def isValid(s):
    st = []

    for c in s:
        if c == '{' or c == '(' or c == '[':
            st.append(c)
            print(st)
        else:
            if not st:
                return False
            if c == '}' and st[-1] != '{':
                return False
            if c == ']' and st[-1] != '[':
                return False
            if c == ')' and st[-1] != '(':
                return False
            st.pop()
    return not st
