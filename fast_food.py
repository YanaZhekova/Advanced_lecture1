from collections import deque

quantity_of_food = int(input())
orders = input().split(" ")
queue = deque()

for order in orders:
    queue.append(int(order))

print(max(queue))
done_all_orders = True
while queue:
    first_order = queue.popleft()
    if quantity_of_food >= first_order:
        quantity_of_food -= first_order
    else:
        done_all_orders = False
        queue.appendleft(first_order)
        break

if done_all_orders:
    print("Orders complete")
else:
    print(f"Orders left: ", end="")
    for o in queue:
        print(o, end=" ")