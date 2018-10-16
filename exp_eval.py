from stack_array import Stack

# You do not need to change this class
class PostfixFormatException(Exception):
    pass

def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    operators = ["<<", ">>", "**", "*", "/", "+", "-"]
    equation = input_str.split()
    stack = Stack(len(equation))
    for i in range(len(equation)):
        if equation[i].isdigit():
            stack.push(equation[i])
        elif equation[i] in operators:
            if stack.size() < 2:
                raise PostfixFormatException("Insufficient operands")
            first_num = stack.pop()
            second_num = stack.pop()
            if first_num == "0" and equation[i] == "/":
                raise ValueError
            if ("." in first_num or "." in second_num) and (equation[i] == "<<" or equation[i] == ">>"):
                raise PostfixFormatException("Illegal bit shift operand")
            total = eval(str(second_num) + str(equation[i]) + str(first_num))
            stack.push(str(total))
        else:
            raise PostfixFormatException("Invalid token")
    if stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return(float(stack.peek()))


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    order_of_op = {
    '<<' : 4,
    '>>' : 4,
    '**' : 3, 
    '*' : 2, 
    '/' : 2, 
    '+' : 1, 
    '-' : 1,
    '(' : 0,
    ')' : 0
    }
    rpn_exp = []
    equation = input_str.split(' ')
    stack = Stack(len(equation))
    for i in range(len(equation)):
        if equation[i].isdigit():
            rpn_exp.append(equation[i])
        elif equation[i] == '(':
            stack.push(equation[i])
        elif equation[i] == ')':
            while stack.peek() != '(':
                rpn_exp.append(stack.pop())
            stack.pop()
        elif equation[i] in order_of_op:
            for j in range(stack.size(), 0, -1):
                if order_of_op[stack.items[j-1]] == 0:
                    break
                if order_of_op[equation[i]] == 3:
                    if order_of_op[equation[i]] < order_of_op[stack.items[j-1]]:
                        rpn_exp.append(stack.pop())
                elif order_of_op[equation[i]] <= order_of_op[stack.items[j-1]]:
                    rpn_exp.append(stack.pop())
            stack.push(equation[i])
    while stack.size() != 0:
        rpn_exp.append(stack.pop())
    return(' '.join(rpn_exp))
    





def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    equation = input_str.split(' ')
    stack = Stack(len(equation))
    for i in range(len(equation)-1, -1, -1):
        if equation[i].isdigit():
            stack.push(equation[i])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            combine =  op1 + " " + op2 + " " + equation[i]
            stack.push(combine)
    return(stack.peek())

