n = int(input())
stack = []
low = []

for i in range(n):
    temp = input()
    if 'PUSH' in temp:
        stack.append(int(temp.split()[1]))
        if not low or stack[-1] < low[-1]:
            low.append(stack[-1])
    elif 'POP' in temp:
        if stack[-1] == low[-1]:
            low.pop()
        stack.pop()
    elif 'MIN' in temp:
        print(low[-1])

# 11     
# PUSH 5
# PUSH 7
# PUSH 3
# PUSH 8
# PUSH 10
# MIN
# POP
# POP
# MIN
# POP
# MIN