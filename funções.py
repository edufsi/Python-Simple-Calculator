import re

def get_invalid_chars(algo):
    equacao = re.compile(r'(?:(?:\d+\.?\d*0)|(?:\d+\.?\d*)?x)[+\-=\./]')
    equation = re.findall(equacao, algo)
    print(equation)

get_invalid_chars('x=')