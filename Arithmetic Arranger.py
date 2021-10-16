import operator

def arithmetic_arranger(problems, sol = False):
    arranged_problems = ""
    num1 = ""
    num2 = ""
    lines = ""
    sum = ""

    for ps in problems:
      try:
        if len(problems) > 5:
            # print(len(problems))
            raise IndexError
      except IndexError:
        return "Error: Too many problems."
        break
      p = ps.split(" ")
      try:
        n1 = int(p[0])
        n2 = int(p[2])
        if p[1] != "-" and p[1] != "+":
          raise SyntaxError
        if len(p[0]) == 0 or len(p[2]) == 0:
          raise ValueError
      except ValueError:
        return "Error: Numbers must only contain digits."
        break
      except IndexError:
        return "Error: Operator must be '+' or '-'."
        break
      except SyntaxError:
        return "Error: Operator must be '+' or '-'."
        break

      try:
        if len(p[0]) > 4 or len(p[2]) > 4:
          raise SyntaxError
      except SyntaxError:
        return "Error: Numbers cannot be more than four digits."
        break
        # print(ps)

      if p[1] == "+":
        res = operator.add(n1, n2)
      elif p[1] == "-":
        res = operator.sub(n1,n2)
        
      if len(p[0]) >= len(p[2]):
        long = len(p[0]) #length of the longer number. an int
        less = len(p[2]) # length of the lesser number
        s = long + 2 # length of the function
        sn = s - less - 1 # no of spaces for line 2
        sr = s - len(str(res)) # no of spaces for results 
                
        lin1 = "  " + p[0] # spaces for the first line. trype str
        lin2 = p[1] + (sn*" ") + p[2]
        line = s*"-"
        lineres = sr*" " + str(res)
                
                
      elif len(p[2]) > len(p[0]):
        long = len(p[2]) #length of the longer number. an int
        less = len(p[0]) # length of the lesser number
        s = long + 2 # length of the function
        sn = s - less # no of spaces for line 1
        sr = s - len(str(res)) # no of spaces for results
                
        lin1 = (sn*" ") + p[0]
        lin2 = p[1] + " " + p[2]
        line = s*"-"
        lineres = sr*" " + str(res)

      if ps != problems[-1]:
        num1 += lin1 + 4*" "
        num2 += lin2 + 4*" "
        lines += line + 4*" "
        sum += lineres + 4*" "
      else:
        num1 += lin1
        num2 += lin2
        lines += line
        sum += lineres

    if len(num1) == 0 or len(num2) == 0:
      arranged_problems = ""
    else:
      if sol == True:
          arranged_problems = num1 + "\n" + num2 + "\n" + lines + "\n" + sum
      else:
          arranged_problems = num1 + "\n" + num2 + "\n" + lines


    return arranged_problems
