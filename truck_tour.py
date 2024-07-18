from collections import deque

pump_station = int(input())
pumps = deque()

for i in range(pump_station):
    pump_data = [int(x) for x in input().split()]
    pumps.append(pump_data)

for s in range(pump_station):
    tank = 0
    failed = False
    for fuel, distance in pumps:
        tank += fuel
        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        pumps.append(pumps.popleft())
    else:
        print(s)
        break
