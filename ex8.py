def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]

ci = 0;
def opz( str, i,  arr):
    ci = i
    print('ci',ci)
    if str[ci] == 'A': #сигнал о встрече массива
        ci -= 1;
        a = int(opz(str, ci, arr)); #ищем индекс одномерного массива
        ci -= 1;
        print( "Вы взяли в массиве элемент со значением " , arr[a]);
        return arr[a];
    
    if str[ci] == '+': #встретили плюс, начинаем искать операнды
        ci -= 1; 
        a2 = opz(str, ci, arr);  a1 = opz(str, ci, arr); return a1+a2;
    
    if str[ci] == '-': #аналогично для остальных операндов
        ci -= 1;
        a2 = opz(str, ci, arr);  a1 = opz(str, ci, arr); return a1-a2;
    
    if str[ci] == '*':
        ci -= 1;
        a2 = opz(str, ci, arr);  a1 = opz(str, ci, arr); return a1*a2;
    
    if str[ci] == '/':
        ci -= 1;
        a2 = opz(str, ci, arr);    a1 = opz(str, ci, arr); return a1/a2;
    
    if str[ci] == '^':
        ci -= 1;
        a2 = opz(str, ci, arr);   a1 = opz(str, ci, arr);   y = a1;
        for j in range(1, a2):
            y *= a1;
        return y;
    
    #собираем число из цифр по схеме Горнера
    ci -= 1;
    x = int(str[ci] - 48);
    if(ci > 0):
        while((ci > 0) & (str[ci-1] != ' ') & (str[ci-1] != '*') & (str[ci-1] != '/') & (str[ci-1] != '^') & (str[ci-1] != '+') & (str[ci-1] != '-') & (str[ci-1] != 'A')):
            x = x + (int(str[ci-1] - 48)) * 10;
            ci -= 1;
        
    ci -= 1;
    return x;



def mass(input, a = 2, b = 3, c = 4 ):
    arr = [[[0 for col in range(c)]for row in range(b)] for x in range(a)]

    counter = 1;


    for i in range(a):
        for j in range(b):
            for k in range(c):
                arr[i][j][k] = counter; #заполняем массив числами
                print ( str(arr[i][j][k]) , end = ' ');
                counter = counter + 1;
            print()
        print()
    
    arr2 = [0 for col in range(a*b*c)]

    for i in range(0, a):
        for j in range (0, b):
            for k in range(0,c):
                arr2[i*b*c+j*c+k] = arr[i][j][k]; #преобразуем трехмерный массив в одномерный
                print ( str(arr2[i*b*c+j*c+k]) +' ' );
            
    
    output = []; #выходная строка
    s: list = []; #стек
    

    k = 0; #счетчик выходной строки
    x = 0; #флаг о встрече точки
    count = 0; #cчетчик квадратных скобок
    for i in range (0,len(input)):
        if(x == 1):
            break;

        if input[i] == '+': #закидываем в стек, если он пуст
            if(len(s) == 0): #иначе выбрасываем из стека в выходную строку все, что больше или равно
                s.append(input[i]) # по приоритету, и только потом записываем в стек
                                # аналогично для остальных операций
            else:
                while(peek(s) == '^'):
                    output.append(  s.pop()); k = k + 1;
                
                if((peek(s) == '*') | (peek(s) == '/')):
                    output.append(  s.pop()); k = k + 1;
                
                if((peek(s) == '-') | (peek(s) == '+')):
                    output.append(  s.pop()); k = k + 1;
                
                s.append(input[i])
            
            break;
        
        if input[i] == '-':
            if(len(s) == 0):
                s.append(input[i])
            
            else:
                while(peek(s) == '^'):
                    output.append( s.pop()); k = k + 1;
                
                if((peek(s) == '*') | (peek(s) == '/')):
                    output.append( s.pop()); k = k + 1;
                
                if((peek(s) == '-') | (peek(s) == '+')):
                    output.append( s.pop()); k = k + 1;
                
                s.append(input[i])
            
            break;
        
        if input[i] == '*':
            if(len(s) == 0):
                s.append(input[i])
            
            else:
                while(peek(s) == '^'):
                    output.append(s.pop()); k = k + 1;
                
                if((peek(s) == '*') | (peek(s) == '/')):
                    output.append(s.pop()); k = k + 1;
                
                s.append(input[i])
            
            break;
        
        if input[i] == '/':
            if(len(s) == 0):
                s.append(input[i])
            
            else:
                while(peek(s) == '^'):
                    output.append(s.pop()); k = k + 1;

                if((peek(s) == '*') | (peek(s) == '/')):
                    output.append(s.pop()); k = k + 1;
                
                s.append(input[i])
            
            break;
        
        if input[i] == '^':
            s.append(input[i])
            break;
        
        if input[i] == '[': #обнаружение индекса трехмерного массива
            s.append(input[i]);  count = count+1;
            break;
        
        if input[i] == ']':
            while(peek(s) != '['):
                output.append( s.pop()); k = k + 1
            
            s.pop()
            if(count == 1):  #если встретился первый индекс 3-мерного массива
                output.append(b+48);
                output.append(" ")
                output.append("*")
                output.append(c+48)
                output.append(" ")
                output.append("*")
            
            if(count == 2):  #если встретился второй индекс 3-мерного массива
                output.append(c+48);

                print (output[k]);
                output.append(" ")
                output.append("*")
                output.append("+")
            
            if(count == 3):  #если встретился третий индекс 3-мерного массива
                output.append( '+'); k = k + 1;
                output.append( 'A'); k = k + 1;
            
            break;
        
        if input[i] == '(':
            s.append(input[i])
            break;
        
        if input[i] == ')':
            while True:
                output.append( s.pop()); k = k + 1;
                if peek(s) == '(':
                    break;            
        
            s.pop()
            break;
        
        if input[i] == 'A':
            output.append( input[i]);  count = 0; k = k + 1;
            break;
        
        if input[i] == '.':
            x = 1;
            while(len(s) > 0):
                output.append( s.pop()); k = k + 1;
            
            break;

        output.append( input[i]);  k = k + 1; #если найден конец числа, то ставим пробел
        if((input[i+1] == 'A') | (input[i+1] == '*') | (input[i+1] == '/') | (input[i+1] == '^') | (input[i+1] == '+') |
           (input[i+1] == '-') | (input[i+1] == '.') | (input[i+1] == ')') | (input[i+1] == ']')):
            output.append( ' '); k = k + 1;
            

    print(output);

    k = len(input)
    k = k - 1;
    #print()
    print(k)
    
    print (opz(output, k, arr2));
    return 0;



s = "A[1][0][3]+7."

mass(s)
print(mass(s))
