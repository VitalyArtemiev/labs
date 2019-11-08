import string, operator
opsa = {'|': operator.neg, '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}

def evalRPN(s):
    while True:
      try:
        st = []
        for tk in str.split(s):
          if tk == '|':
              x = st.pop()
              z = opsa[tk](x)
          elif tk in opsa:
            y,x = st.pop(), st.pop()
            z = opsa[tk](x, y)
          else:
            z = float(tk)
          st.append(z)
        assert len(st)<=1
        if len(st)==1:
            print(st.pop())
            break
      except Exception as e:
        print('error', str(e))
        break



evalRPN("2 2 | 2 6 * 4 / ^ ^ ")
