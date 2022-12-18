import operator as op

#Add new operators here if needed, arrange_problems() refers to this for calculations
operators = {
    "+" : op.add,
    "-" : op.sub
}


error_codes = {
    1 : "Error: Too many problems.",
    2 : "Error: Operator must be '+' or '-'.",
    3 : "Error: Numbers must only contain digits.",
    4 : "Error: Numbers cannot be more than four digits."
}


def check_errors(problems):
    #Check for too many problems
    if len(problems) > 5:
        return 1
        
    for expression in problems:
        operand1, operator, operand2 = expression.split()

        #Check for valid operators
        if operator != '+' and operator != '-':
            return 2
        
        #Operands must be numbers
        if not operand1.isnumeric() or not operand2.isnumeric():
            return 3        

        #Operands must not be longer than four digits
        if len(operand1) > 4 or len(operand2) > 4:
            return 4        

    return 0


def arrange_problems(problems, calculate_answer):    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for expression in problems: 
        operand1, operator, operand2 = expression.split()
        
        width = max(len(operand1), len(operand2)) + 2
        
        #Format the expression 
        line1 += (width - len(operand1)) * " " + operand1
        line2 += operator + " " + (width - 2 - len(operand2)) * " " + operand2
        line3 += width * "-"

        #Calculate answer if specified
        if calculate_answer:
            answer = str(operators[operator] (int(operand1),  int(operand2)))
            line4 += (width - len(answer)) * " " + answer

        #Add 4 spaces between problems
        if expression != problems[len(problems)-1]:
            line1 += 4 * " "
            line2 += 4 * " "
            line3 += 4 * " "
            if calculate_answer:
                line4 += 4 * " "

    line1 += "\n"
    line2 += "\n"    
    if calculate_answer:
        line3 += "\n"

    return line1 + line2 + line3 + line4


def arithmetic_arranger(problems, calculate_answer = False):    
    error_code = check_errors(problems)
    if error_code > 0:
        return error_codes[error_code]

    return arrange_problems(problems, calculate_answer)