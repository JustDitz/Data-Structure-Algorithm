n = int(input())
queue = []

for i in range(n):
    temp = input()
    if '+' in temp:
        queue.append(int(temp[1:]))
        print(len(queue))
    elif not queue:
        break
    else:
        print(queue.pop(0))
print(queue)