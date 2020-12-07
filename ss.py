V, E = map(int, input().split())
G = [[] for _ in range(V)]

for _ in range(E) :
    u, v = map(int, input().split())
    G[u-1].append(v)
    G[v-1].append(u)

visited = [0] * V
cnt = 0
while 0 in visited :

    first_idx = visited.index(0) + 1
    stack = [first_idx]

    v = first_idx
    visited[first_idx-1] = 1

    while stack :
        for w in G[v-1] :
            if visited[w-1] == 0 :
                stack.append(w)
                visited[w-1] = 1
                v = w
                break
        else :
            v = stack.pop()

    cnt += 1

print(cnt)