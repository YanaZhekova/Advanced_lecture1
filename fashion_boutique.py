box_of_clothes = list((int(x) for x in input().split(" ")))
capacity = int(input())
sum_clothes = 0
racks = 0
while box_of_clothes:
    first_clothes = box_of_clothes.pop()
    sum_clothes += first_clothes
    if capacity == sum_clothes:
        sum_clothes = 0
        racks += 1
    elif capacity < sum_clothes:
        sum_clothes = first_clothes
        racks += 1

if sum_clothes != 0:
    racks += 1
print(racks)
