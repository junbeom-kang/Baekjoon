from sys import stdin, stdout

N = 20
s = 0
t = int(stdin.readline())

for _ in range(t):
    op = stdin.readline().split()

    if op[0] == "add":
        x = int(op[1]) - 1
        s = s | (1 << x)
    elif op[0] == "remove":
        x = int(op[1]) - 1
        s = s & ~(1 << x)
    elif op[0] == "check":
        x = int(op[1]) - 1
        res = s & (1 << x)
        stdout.write(("1" if res > 0 else "0") + "\n")
    elif op[0] == "toggle":
        x = int(op[1]) - 1
        s = s ^ (1 << x)
    elif op[0] == "all":
        s = (1 << N) - 1
    else:
        s = 0