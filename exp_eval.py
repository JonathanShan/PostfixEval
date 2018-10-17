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
            try:
                total = eval(str(second_num) + str(equation[i]) + str(first_num))
            except TypeError:
                raise PostfixFormatException("Illegal bit shift operand")
            stack.push(str(total))
        else:
            raise PostfixFormatException("Invalid token")
    if stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    if stack.size() == 0:
        return ""
    return float((stack.peek()))


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
        if len(input_str) == 0:
            return ""
        if equation[i].isdigit():
            rpn_exp.append(equation[i])
        elif equation[i] == '(':
            stack.push(equation[i])
        elif equation[i] == ')':
            while stack.peek() != '(':
                rpn_exp.append(stack.pop())
            stack.pop()
        elif order_of_op[equation[i]] == 3:
            for j in range(stack.size()):
                if order_of_op[equation[i]] < order_of_op[stack.items[j]]:
                    rpn_exp.append(stack.pop())
                else:
                    break
            stack.push(equation[i])
        elif equation[i] in order_of_op:
            for k in range(stack.size(), 0, -1):
                if order_of_op[equation[i]] <= order_of_op[stack.items[k-1]]:
                    rpn_exp.append(stack.pop())
                else:
                    break
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
    for i in range(len(equation), 0, -1):
        if equation[i-1].isdigit():
            stack.push(equation[i-1])
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            combine =  op1 + " " + op2 + " " + equation[i-1]
            stack.push(combine)
    return(stack.pop())

#print(prefix_to_postfix("** * 2 / 5 6 8"))
#print(postfix_eval("3 4 6 ** * 2 5 6 / * 8 ** +"))
#print(postfix_eval("3 4 6 ** * 2 5 6 / 8 ** * +"))
#print(infix_to_postfix("( 2 + 3 ) * 4 - ( 5 - 6 ) * ( 7 + 8 )"))
#postfix_eval("2 3 4 / <<")
#infix_to_postfix("( 3 * 4 ** 6 + ( 2 * ( 5 / 6 ) ** 8 ) )")
#postfix_eval("4 2 >> 2 +")