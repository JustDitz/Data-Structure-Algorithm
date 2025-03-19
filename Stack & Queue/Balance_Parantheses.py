bracket_pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}
x = input()
stack = []

for char in x:
    if char in '({[':
        stack.append(char)
    elif char in ')}]':
        if not stack:
            print("Invalid")
            break
        if stack[-1] == bracket_pairs[char]:
            stack.pop()
        else:
            print("Invalid")
            break

if not stack:
    print ("Valid")

# Input
# [{({})}]

# Output
# Valid

# Input
# {[}

# Output
# Invalid
