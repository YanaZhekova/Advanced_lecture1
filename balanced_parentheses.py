parentheses = input()

par_stack = []
valid_par = False
for index in range(0, len(parentheses), 1):
    par = parentheses[index]
    if len(par_stack) == 0 and (par == "]" or par == "}" or par == ")"):
        valid_par = False
        break
    if par == "(" or par == "[" or par == "{":
        par_stack.append(par)
    elif par == ")":
        last_par = par_stack.pop()
        if last_par == "(":
            valid_par = True
        else:
            valid_par = False
            break
    elif par == "]":
        last_par = par_stack.pop()
        if last_par == "[":
            valid_par = True
        else:
            valid_par = False
            break
    elif par == "}":
        last_par = par_stack.pop()
        if last_par == "{":
            valid_par = True
        else:
            valid_par = False
            break

if not valid_par:
    print("NO")
else:
    print("YES")
