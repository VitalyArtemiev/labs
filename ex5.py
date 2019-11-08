import string, operator
ops = {'=': operator.eq, '|': operator.or_, '&': operator.and_, '!': operator.not_ }
uops = {'!':operator.not_}

def evalRPN(s:str):
    while True:
      try:
        st = []
        for tk in str.split(s):
          if tk in uops:
            y = st.pop()
            z = uops[tk](y)
          elif tk in ops:
            y, x = st.pop(), st.pop()
            z = ops[tk](x,y)
          else:
            z = bool(tk)
          st.append(z)
        assert len(st)<=1
        if len(st)==1:
            print(st.pop())
            break
      except Exception as e:
        print('error', str(e))
        break



evalRPN("t f & t f | t ! & | ")
