example=[[' ','x',' ','x',' '],
        ['x','x','x','x','x'],
        ['x','x','x','x','x'],
        [' ','x','x','x',' '],
        [' ',' ','x',' ',' ']]


def printMatrix(exampleMatrix):
    for x in range(len(exampleMatrix)):
        for y in range(len(exampleMatrix)):
            print(exampleMatrix[x][y], end='')
        print()

printMatrix(example)