while True:
    try: 
        text = input()
        queue_prioritize = []
        queue_text = []

        output = ''
        flag = 0
        for i in range(len(text)):
            if text[i] == '[':
                flag = 1
            elif text[i] == ']':
                flag = 0
            elif not flag:
                queue_text.append(text[i])
            else:
                queue_prioritize.append(text[i])
        
        while queue_prioritize:    
            output += queue_prioritize.pop(0)

        while queue_text:
            output += queue_text.pop(0)
        print(output)
    except EOFError:
        break

# Input
# This_is_a_[Beiju]_text
# [[]][][]Happy_Birthday_to_Tsinghua_University

# Output
# BeijuThis_is_a__text
# Happy_Birthday_to_Tsinghua_University