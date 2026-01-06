def valid(equation):
    #해당 문제는 간결한 코드를 보여주기 위한 답
    equation = equation.replace('=', '==')
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]