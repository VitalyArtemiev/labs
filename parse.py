def parse(s):
    for operator in ["+-", "*/"]:
        depth = 0
        for p in range(len(s)-1, -1, -1):
            if s[p] == ')': depth +=1
            if s[p] == '(': depth -=1
            if not depth and s[p] in operator:
                return [s[p]] + parse(s[:p]) + parse(s[p+1:])
    s = s.strip()
    if s[0] == '(':
        return parse(s[1:-1])
    return [s]
