def arithmetic_arranger(problems,show_result=False):
    number1 = []
    number2 = []
    operator = []
    if len(problems) > 5:
      return ("Error: Too many problems.")
    for i,op in enumerate(problems):
      if (op.find('*') != -1) or (op.find('/') != -1):
          return ("Error: Operator must be '+' or '-'.")           
      elif op.find('+') != -1:
        cont = op.split('+')
        operator.insert(i,'+')
      elif op.find('-') != -1:
        cont = op.split('-')
        operator.insert(i,'-')  
      for n in cont:
          if (n.strip().isdigit()==False):
              return ("Error: Numbers must only contain digits.") 
          if (len(n.strip()) > 4):
              return ("Error: Numbers cannot be more than four digits.")          
      number1.insert(i,cont[0].strip()) 
      number2.insert(i,cont[1].strip()) 
    
    # Printing lines
    #Line 1
    line1=""
    for i in range(len(number1)):
        for spaces in range(2+max(len(number1[i]),len(number2[i]))-len(number1[i])):
             line1 += (' ')
        line1 += (number1[i])
        if (i == len(number1) - 1):
            break
        line1 += ('    ')

    #Line 2
    line2=""
    for i in range(len(number2)):
        line2 += (operator[i])
        for spaces in range(1+max(len(number1[i]),len(number2[i]))-len(number2[i])):
              line2 += (' ')
        line2 += (number2[i])   
        if (i == len(number2) - 1):
            break
        line2 += ('    ')
    
    #Line 3
    line3=""
    for i in range(len(number1)):
        for spaces in range(2+max(len(number1[i]),len(number2[i]))):
            line3 += ('-')
        if (i == len(number1) - 1):
            break
        line3 += ('    ')  
    
    # Put lines together
    arranged_problems = line1 + "\n" + line2 + "\n" + line3
    
    # Print (if false)
    if show_result==False:
        return arranged_problems
    
    #Line 4 (if true) 
    elif show_result:
        line4 = ""
        result = []
        for i in range(len(number1)):
            if (operator[i]=="+"):
                result.append(int(number1[i])+int(number2[i]))
            else: 
                result.append(int(number1[i])-int(number2[i]))    
            for spaces in range(2+max(len(number1[i]),len(number2[i]))-len(str(result[i]))):
                line4 += (' ')
            line4 += (str(result[i]))  
            if (i == len(number1) - 1):
                break
            line4 += ('    ')   
        arranged_problems += "\n" + line4
        return arranged_problems
