import math

n = int(input())
numbers_stack = []
for i in range(n):

    query = input().split(" ")
    command = int(query[0])
    if command == 1:
        numbers_stack.append(int(query[1]))
    elif command == 2:
        if len(numbers_stack) >= 1:
            numbers_stack.pop()
    elif command == 3:
        if len(numbers_stack) >= 1:
            print(max(numbers_stack))
    elif command == 4:
        if len(numbers_stack) >= 1:
            print(min(numbers_stack))

for num in range(len(numbers_stack) - 1, -1, -1):
    if num == 0:
        print(numbers_stack[num], end="")
    else:
        print(numbers_stack[num], end=", ")
