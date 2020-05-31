import re

def arithmetic_arranger(problems, optional= False):
  result_list = []
  split_list = []
  a = ""
  b = ""
  c = ""
  d = ""

  for i in problems:
    
    try:
      result = eval(i)
      result_list.append(result) # for solutions 
      split_list.append(re.split('([+-/*])', i.replace(" ",""))) # for splitting the list wrt operators
    except:
      return "Error: Numbers must only contain digits."
  
  if len(split_list)>5:
    return "Error: Too many problems."

  for i in range (len(split_list)):
    if str(split_list[i][1]) in '*/':
      return "Error: Operator must be '+' or '-'."

#Error: Numbers cannot be more than four digits.
  for i in range(len(split_list)):
    if len(split_list[i][0])>4 or len(split_list[i][2])>4:
      return "Error: Numbers cannot be more than four digits."


  for i in range (len(split_list)):

    width = max(len(split_list[i][0]),(len(split_list[i][2])))
    operator_width = width- (len(split_list[i][2]))+1
    b1 = str(split_list[i][1])+" "*operator_width+ str(split_list[i][2])
    a1 =  f"{split_list[i][0]}".rjust(width+2)
    btw_length = 4
    c1 = ("-"*(width+2)).rjust(width+2)
    if result_list[i]<0:
      abs_result = abs(result_list[i])
      d1 = f"-{abs_result}".rjust(width+2)
    else:
      d1 = f"{result_list[i]}".rjust(width+2)

    if i != (len(split_list)-1):
      b += b1+ btw_length*" "
      a += a1 + btw_length*" "
      c += c1 + btw_length*" "
      d += d1 + btw_length*" "
    else:
      b += b1
      a += a1
      c += c1
      d += d1


  
  e = f"{a}\n{b}\n{c}"
  f = f"{a}\n{b}\n{c}\n{d}"


  if optional == True:
    return f

  return e   




