text = input()
parentheses_stack = []

for index in range(len(text)):
    if text[index] == "(":
        parentheses_stack.append(index)
    elif text[index] == ")":
        start_index = parentheses_stack.pop()
        result = slice(start_index, index + 1)
        print(text[result])
