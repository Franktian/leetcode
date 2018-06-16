def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    st = []
    
    for t in tokens:
        if t not in ["+", "-", "*", "/"]:
            st.append(int(t))
        else:
            right = st.pop()
            left = st.pop()
            
            if t == '+':
                st.append(left + right)
            elif t == '-':
                st.append(left - right)
            elif t == '*':
                st.append(left * right)
            else:
                if left * right < 0:
                    st.append(-(abs(left)/abs(right)))
                else:
                    st.append(left/right)
    return st.pop()
