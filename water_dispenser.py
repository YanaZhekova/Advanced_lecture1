from collections import deque

dispenser = int(input())

name = input()
line = deque()

while not name == "Start":
    line.append(name)
    name = input()

command = input()

while not command == "End":

    if command.isdigit():
        liters = int(command)
        person = line.popleft()
        if dispenser >= liters:
            dispenser -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    else:
        liters_to_fill = int(command.split(" ")[1])
        dispenser += liters_to_fill
    command = input()

print(f"{dispenser} liters left")