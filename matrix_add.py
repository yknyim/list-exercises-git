number1 = [
    [4,7],
    [1,3]
]

number2 = [
    [2,6],
    [8,3]
]

matrix = [
    [],
    []
]

for x in number1:
    matrix = number1.index(x)
    for y in number2:
        matrix = number2.index(y)


print(matrix)