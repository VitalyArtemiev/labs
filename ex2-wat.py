def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]


def toRPN(s: str):
    ops = ['+', '-', '/', '*', '^']
    ops1 = ['+', '-']
    ops2 = ['/', '*']
    ops3 = ['^']

    laops = ['-']
    p: str = ""
    l: list = []

    s.replace('+-', "-")
    s.replace('-', "+-")

    result: str = ""
    for c in s:
        print(c)
        if c.isdigit():
            result += c + ' '

        elif c in ops:
            p = peek(l)
            if (p in ops):
                while  (ops.index(p) >= ops.index(c) or (p in ops1 and c in ops1 and p in laops) or (p in ops2 and c in ops2 and p in laops)) and (len(l) > 0):
                    result += l.pop() + ' '
            l.append(c)

        elif c == '(':
            l.append(c)

        elif c == ')':
            p = l.pop()
            while p != '(':
                print(p)
                result += p + ' '
                if len(l) != 0:
                    p = l.pop()
                else:
                    print(result)
                    print("Error")

    while len(l) > 0:
        result += l.pop() + ' '

    return result


def run():
    s = "1+2-3*5/6"
    print(toRPN(s))


s = "1 + 2 *3/(5-6)"
print(toRPN(s))
