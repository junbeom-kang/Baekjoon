import sys
stack=[[]for _ in range(100)]
i=0
first = {'*': 2, '/': 2, '+': 1, '-': 1}
data=['(']
data.extend(list(sys.stdin.readline().strip()))
data.append(')')
def divide(n):
    global i
    while data[i]!=')':
        if data[i]=='(':
            i+=1
            divide(i)
            continue
        elif 'A' <= data[i] <= 'Z':
            print(data[i],end='')
            i+=1
            continue
        else:
            if not stack[n]:
                stack[n].append(data[i])
            else:
                while stack[n] and first[data[i]] <= first[stack[n][-1]]:
                    print(stack[n].pop(), end='')
                stack[n].append(data[i])

            i+=1
    while stack[n]:
        print(stack[n].pop(),end='')
divide(0)