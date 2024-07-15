text = list(input())

reversed_text = []

for index in range(len(text)-1,-1,-1):
    reversed_text.append(text[index])

print("".join(reversed_text))

