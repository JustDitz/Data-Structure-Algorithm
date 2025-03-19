# No 5 PRN Notation
n = int(input())
output = []

def tingkatan(x):
    if x in ('+', '-'):
        return 1
    if x in ('*', '/'):
        return 2
    if x in ('^'):
        return 3
    return 0

for _ in range (n):
    temp = input()
    main_stack = []
    temp_output = ""
    
    for i in range (len(temp)):
        if temp[i].isalpha():
            temp_output += temp[i]
        elif temp[i] == '(':
            main_stack.append(temp[i])
        elif temp[i] == ')':
            while main_stack and main_stack[-1] != '(':
                temp_output += main_stack.pop()
            main_stack.pop()
        else: # Operator
            while main_stack and tingkatan(main_stack[-1]) >= tingkatan(temp[i]):
                temp_output += main_stack.pop()
            main_stack.append(temp[i])
       
    while main_stack:
        temp_output += main_stack.pop()
         
    output.append(temp_output)

for i in output:
    print(i)
    
# Input:
# 3
# (a+(b*c))
# ((a+b)*(z+x))
# ((a+t)*((b+(a+c))^(c+d)))

# Output:
# abc*+
# ab+zx+*
# at+bac++cd+^*