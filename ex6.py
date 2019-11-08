def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]


def ifToRPN(inputstr):
    # char inputstr[256] #входная строка
    # char s[256] #стек
    s: list = []
    x = 0  # флаг

    
    result = "";
    
    # j = 0  # счетчик стека
    i = 0  # счетчик цикла
    while (i < len(inputstr)):
        #result += inputstr[i]'\
        if (x == 1):  # встретилась ли точка
            break

        if inputstr[i] == 'i':  # перепрыгиваем "если"
            i += 3
            continue

        if inputstr[i] == 't':  # перепрыгиваем "то"
            i += 4
            result +="'p2!"  # указатель на выражение 2
            continue

        if inputstr[i] == 'e':  # перепрыгиваем "иначе"
            result +="p3#"  # указатель на выражение 3
            i += 4
            continue

        if inputstr[i] == ' ':  # разделитель
            while (len(s) > 0):
                result +=s.pop()

            i = i + 1
            continue

        if inputstr[i] == '+':  # обычные арифметические операции
            if (len(s) == 0):
                s.append(inputstr[i])

            else:
                while (peek(s) == '^'):
                    result +=s.pop()

                if (peek(s) == '*') | (peek(s) == '/'):
                    result +=s.pop()

                if (peek(s) == '-') | (peek(s) == '+'):
                    result +=s.pop()

                s.append(inputstr[i])

            i = i + 1
            continue

        if inputstr[i] == '-':
            if (len(s) == 0):
                s.append(inputstr[i])

            else:
                while (peek(s) == '^'):
                    result +=s.pop()

                if (peek(s) == '*') | (peek(s) == '/'):
                    result +=s.pop()

                if (peek(s) == '-') | (peek(s) == '+'):
                    result +=s.pop()

                s.append(inputstr[i])

            i = i + 1
            continue

        if inputstr[i] == '*':
            if (len(s) == 0):
                s.append(inputstr[i])

            else:
                while (peek(s) == '^'):
                    result +=s.pop()

                if (peek(s) == '*') | (peek(s) == '/'):
                    result +=s.pop()

                s.append(inputstr[i])

            i = i + 1
            continue

        if inputstr[i] == '/':
            if (len(s) == 0):
                s.append(inputstr[i])

            else:
                while (peek(s) == '^'):
                    result +=s.pop()

                if (peek(s) == '*') | (peek(s) == '/'):
                    result +=s.pop()

                s.append(inputstr[i])

            i = i + 1
            continue

        if inputstr[i] == '^':
            s.append(inputstr[i])

            i = i + 1
            continue

        if inputstr[i] == '{':
            s.append(inputstr[i])
            i = i + 1
            continue

        if inputstr[i] == '}':
            while (peek(s) != '{'):
                result +=s.pop()

            s.pop()
            result +="'"
            i = i + 1
            continue

        if inputstr[i] == '=':
            s.append(inputstr[i])
            i = i + 1
            continue

        if inputstr[i] == '(':
            s.append(inputstr[i])
            i = i + 1
            continue

        if inputstr[i] == ')':
            while (peek(s) != '('):
                result +=s.pop()

            s.pop()
            i = i + 1
            continue

        if inputstr[i] == '.':
            x = 1
            while (len(s) > 0):
                result +=s.pop()

            continue

        result +=inputstr[i]
        i = i + 1

    return result


s = "if (a=b) then {a=a+2} else {a=b}."
print(ifToRPN(s))
