def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]


def toRPN(s: str):
    s = list(s)

    ops = ['|','+', '-', '/', '*', '^']
    laops = ['|','+', '-', '/', '*']
    p: str = ""
    l: list = []

    if s[0] == '-':
        s[0] = '|'

    for i in range(1, len(s)-1):
        if ((s[i-1] in ops) or (s[i-1] == '(')) and (s[i] == '-'):
            s[i] = '|'

    print(s)

    result: str = ""
    for c in s:
        #print(c)
        if c.isdigit():
            result += c + ' '

        elif c == '(':
            l.append(c)

        elif c == ')':
            p = l.pop()
            while p != '(':
                #print(p)
                result += p + ' '
                if len(l) != 0:
                    p = l.pop()
                else:
                    print(result)
                    raise Exception("error with parenthesis")

        elif c in ops:
            p = peek(l)

            while (p in ops) and ((ops.index(p) > ops.index(c)) or
                                  (ops.index(p) == ops.index(c) and p in laops)) \
                    and (len(l) > 0):
                result += l.pop() + ' '
                p = peek(l)

            l.append(c)

        else:
            raise Exception("error in symbols")

    while len(l) > 0:
        result += l.pop() + ' '

    return result


def run():
    s = "1+2-3*5/6"
    print(toRPN(s))

c = "2^(-2)^(2*6/4)"
print(toRPN(c))
