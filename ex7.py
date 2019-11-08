def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]


def cycleRPN(input):
    s: list = [];
    x = 0;

    result = "";
    i = 0;  # счетчик елементов строки
    f1 = 0;  # флаг второй запятой
    f2 = 0;  # флаг тела цикла
    while (i < len(input)):
        if (x == 1):
            break;

        if input[i] == 'w':  # встретился while
            f1 = -1;  # вторая запятая не встретится
            f2 = 0;  # обнуляем флаг цикла
            i += 5;
            continue;

        if input[i] == 'd':  # встретился do
            i += 2;
            result += "p2!";  # указывает на выражение после цикла
            continue;

        if input[i] == 'f':  # встретился for
            i += 3;
            f1 = 0;  # ожидаем, что встретятся запятые
            f2 = 0;  # обнуляем флаг цикла
            continue;

        if input[i] == ',':  # встретили запятую
            f1 = f1 + 1;
            while (peek(s) != '('):
                result += s.pop();

            result += "'";
            if (f1 == 2):  # если встретилась вторая запятая, то выводим
                result += "p3!p2#";  # указатель на выражение после цикла 
            i += 2;  # и указатель на тело цикла соответственно
            continue;

        if input[i] == ' ':  # разделитель
            i = i + 1;
            continue;

        if input[i] == '+':  # обработка простых арифметический операций
            if (len(s) == 0):
                s.append(input[i])

            else:
                while (peek(s) == '^'):
                    result += s.pop();

                if ((peek(s) == '*') | (peek(s) == '/')):
                    result += s.pop();

                if ((peek(s) == '-') | (peek(s) == '+')):
                    result += s.pop();

                s.append(input[i])

            i = i + 1;
            continue;

        if input[i] == '-':
            if (len(s) == 0):
                s.append(input[i])

            else:
                while (peek(s) == '^'):
                    result+= s.pop()

                if ((peek(s) == '*') | (peek(s) == '/')):
                    result+= s.pop()

                if ((peek(s) == '-') | (peek(s) == '+')):
                    result+= s.pop()

                s.append(input[i])

            i = i + 1;
            continue;

        if input[i] == '*':
            if (len(s) == 0):
                s.append(input[i]);

            else:
                while (peek(s) == '^'):
                    result += s.pop()

                if ((peek(s) == '*') | (peek(s) == '/')):
                    result+= s.pop()

                s.append(input[i]);

            i = i + 1;
            continue;

        if input[i] == '/':
            if (len(s) == 0):
                s.append(input[i]);

            else:
                while (peek(s) == '^'):
                    result+= s.pop()

                if ((peek(s) == '*') | (peek(s) == '/')):
                    result+= s.pop()

                s.append(input[i]);

            i = i + 1;
            continue;

        if input[i] == '^':
            s.append(input[i]);
            i = i + 1;
            continue;

        if input[i] == '{':  # начало нового выражения
            f2 = f2 + 1;
            if ((f2 == 1) & (f1 == 2)):  # если цикл for
                result += "p0#";  # указывает на условие
            s.append(input[i]);
            i = i + 1;
            continue;

        if input[i] == '}':
            while (peek(s) != '{'):
                result+= s.pop()

            s.pop()
            result += "'";
            if ((f2 == 1) & (f1 == 2)):  # если цикл for
                result += "p1#";  # указывает на выражение 2
            if ((f2 == 1) & (f1 == -1)):  # если цикл while
                result += "p0#";  # указывает на условие
            i = i + 1;
            continue;

        if input[i] == '>':
            s.append(input[i]);
            i = i + 1;
            continue;

        if input[i] == '<':
            s.append(input[i]);
            i = i + 1;
            continue;

        if input[i] == '=':
            s.append(input[i])
            i = i + 1;
            continue;

        if input[i] == '(':
            s.append(input[i]);
            i = i + 1;
            continue;

        if input[i] == ')':
            while (peek(s) != '('):
                result+= s.pop()

            s.pop()
            i = i + 1;
            result += "'";
            continue;

        if input[i] == '.':
            x = 1;
            while (len(s) > 0):
                result += s.pop()

            continue;

        result += input[i];
        i = i + 1;

    return result;


s = "while (a<5) do {a++}."
print(cycleRPN(s))
