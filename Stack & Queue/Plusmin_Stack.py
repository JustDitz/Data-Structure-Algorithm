n = int(input())
stack = []

for i in range(n):
    temp = input()
    if '+' in temp:
        stack.append(int(temp[1:]))
        print(len(stack))
    elif not stack:
        break
    else:
        print(stack.pop())
print(stack)

# Input
# 5
# +1
# +2
# +3
# -
# +7

# Output 
# 1
# 2
# 3
# 3
# [1, 2, 7]