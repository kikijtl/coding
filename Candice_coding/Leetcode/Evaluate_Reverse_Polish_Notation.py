'''Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''
import math

def evalRPN(tokens):
    if not tokens:
        return
    n = len(tokens)
    stack = []
    for i in range(n):
        if tokens[i] == "+":
            num1 = stack.pop()
            num2 = stack.pop()
            tmp = num2 + num1
            #print tmp
            stack.append(tmp)
        elif tokens[i] == "-":
            num1 = stack.pop()
            num2 = stack.pop()
            tmp = num2 - num1
            #print tmp
            stack.append(tmp)
        elif tokens[i] == "*":
            num1 = stack.pop()
            num2 = stack.pop()
            tmp = num2 * num1
            #print tmp
            stack.append(tmp)
        elif tokens[i] == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            if num2 * num1 < 0:
                tmp = abs(num2) / abs(num1) * (-1)
                '''in python, (-7)/2=-4'''
            else:
                tmp = num2 / num1
            '''if we need tmp to be float,
            we can use tmp = num2 / float(num1)'''
            #print tmp
            stack.append(tmp)
        else:
            stack.append(int(tokens[i]))
    return stack[0]

if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print evalRPN(tokens)