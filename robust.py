def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]


def toRPN(s: str):
    ops = ["if", "(", ")","then","else","|","&","!","<",">","=","+","-", "*", "/", "^"]
    opp = [0,     0,   1,  1,     1,     2,  3,  4,  5,  5,  5,  6,  6,   7,   7,   8]

    stk = ["jnt", "jmp"]

    mi = 1


    laops = ['!','+', '-', '/', '*', '|', '&']
    l: list = []
    
    if s[0] == '-':
        s[0] = '!'

    for i in range(1, len(s)-1):
        if ((s[i-1] in ops) or (s[i-1] == '(')) and (s[i] == '-'):
            s[i] = '!'
    

    result: str = ""
    for tk in str.split(s):
        print(tk)
        if tk=='t' or tk=='f' or tk.isdigit():
            result += tk + ' '

        elif tk == ops[1]: # (
            l.append(tk)

        elif tk == ops[2]: # )
            p = l.pop()
            while p != ops[1]: #to (
                #print(p)
                result += p + ' '
                if len(l) != 0:
                    p = l.pop()
                else:
                    print(result)
                    raise Exception("error with parenthesis")

        elif tk == ops[3]: #then
            p = l.pop()
            while p != ops[0]: #to if
                #print(p)
                result += p + ' '
                if len(l) != 0:
                    p = l.pop()
                else:
                    print(result)
                    raise Exception("error with parenthesis")
            p = p + "M" + str(mi)
            l.append(p)


        elif tk == ops[4]: #else
            p = l.pop()
            while not ('ifM'  in p): #to ifm
                #print(p)
                result += p + ' '
                if len(l) != 0:
                    p = l.pop()
                else:
                    print(result)
                    raise Exception("error with parenthesis")
            i = int(p[3:])
            i = i+1
            p = 'ifM' + str(i)
            result +=p + ' '
            result += stk[1] + 'M' + str(i-1) + ' '


        elif tk in ops:
            p = peek(l)

            while (p in ops) and ((opp[ops.index(p)] > opp[ops.index(tk)]) or (opp[ops.index(p)] == opp[ops.index(tk)]
                                                                     and p in laops)) and (len(l) > 0):
                result += l.pop() + ' '
                p = peek(l)

            l.append(tk)

        else:
            raise Exception("error in symbols")


    while len(l) > 0:
        result += l.pop() + ' '

    return result

def run():
    s = "if t then 1 else 2"
    print(toRPN(s))

run()


