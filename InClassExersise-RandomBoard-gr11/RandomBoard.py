import random

def printArray(board):
    for x in range(len(board)):
            print(board[x])

def findSum(board):
    total = 0
    for x in range(10):
        for y in range(10):
            total += board[x][y]
    print(total)

board = [[0 for i in range(10)]for j in range(10)]
for x in range(10):
    for y in range(10):
        board[x][y] = random.randint(0,9)

printArray(board)
findSum(board)
