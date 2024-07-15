numbers = input().split(" ")

numbers_stack = []

for index in range(len(numbers)-1,-1,-1):
    numbers_stack.append(numbers[index])

print(" ".join(numbers_stack))
