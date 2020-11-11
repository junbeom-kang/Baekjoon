def star(n):
    if n == 3:
        return ["***", "* *", "***"]
    n = n // 3
    s = star(n)
    e = [" "*n]*n
    a = list(map(lambda i: ''.join(i), zip(s, s, s)))
    b = list(map(lambda i: ''.join(i), zip(s, e, s)))
    print(a,b)
    print(a+b)
    return a + b + a
print(star(int(input())))
for s in star(int(input())):
    print(s)