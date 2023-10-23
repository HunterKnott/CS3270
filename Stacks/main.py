'''Hunter Knott, Utah Valley University, CS 2420'''
from stack import Stack
from node import StackNode

def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError("The given expression must be a string")
    output = ""
    operator_stack = Stack()
    left_par_count = 0
    right_par_count = 0
    for element in expr:
        if element == " " or element == "\n":
            continue
        # Element is "("
        if element == "(":
            left_par_count += 1
            operator_stack.push(element)
        elif element.isnumeric():
            # Element is a number
            output += element
        elif element == "+" or element == "-" or element == "*" or element == "/":
            # Element is an operator
            while operator_stack.size() > 0 and operator_stack.top() != "(" and operator_stack.precedence[operator_stack.top()] >= operator_stack.precedence[element]:
                output += operator_stack.top()
                operator_stack.pop()
            operator_stack.push(element)
        else:
            # Element is ")"
            right_par_count += 1
            if left_par_count < right_par_count:
                raise SyntaxError("There are too many parentheses")
            while operator_stack.top() != "(":
                output += operator_stack.pop()
            operator_stack.pop()
    if operator_stack.size() > 0:
        output += operator_stack.pop()
    return output

def eval_postfix(expr):
    operand_stack = Stack()
    if expr is None:
        raise ValueError("There is nothing in the expression")
    expr = expr.replace(" ", "")
    num_count = 0
    operator_count = 0
    for element in expr:
        if element.isnumeric():
            num_count += 1
            operand_stack.push(element)
        else:
            operator_count += 1
            if operator_count == num_count:
                raise SyntaxError("There are too many operators in the expression")
            operand1 = operand_stack.pop()
            if operand_stack.top() is None:
                continue
            operand2 = operand_stack.pop()
            operand_stack.push(str(eval(operand2 + element + operand1)))
    return float(eval(operand_stack.pop()))

def main():
    '''Converts infix expressions to postfix using stacks'''
    expressions = []
    with open("data.txt", "r") as file:
        while True:
            line = str(file.readline())
            if not line:
                break
            expressions.append(line.strip())
            postfix_result = in2post(line)
            print("Infix: " + expressions[len(expressions)-1])
            print("Postfix: " + " ".join(postfix_result))
            print("Answer: " + str(eval_postfix(postfix_result)) + "\n")

if __name__ == '__main__':
    main()