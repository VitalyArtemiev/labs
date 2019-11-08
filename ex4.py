def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]


def toRPN(s: str):
    ops = ['=', '|',  '&',  '!']
    laops = []
    l: list = []

    result: str = ""
    for c in s:
        #print(c)
        if c=='t' or c=='f':
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

            while (p in ops) and ((ops.index(p) > ops.index(c))
                                  or (ops.index(p) == ops.index(c) and p in laops)) \
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
    s = ""
    print(toRPN(s))


s = "t&f|(t|f)&!t"
print(toRPN(s))
