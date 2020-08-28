import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

arr = []
arr.append(nums[0])

reverse = []
reverse.append(0)

for i in range(1, N):
    h = nums[i]

    if arr[-1] < h:
        arr.append(h)
        reverse.append(len(arr) - 1)
    else:
        l = 0
        r = len(arr)
        m = 0
        while l < r:
            m = (l + r) // 2
            if arr[m] < h:
                l = m + 1
            else:
                r = m

        arr[r] = h
        reverse.append(r)

print(len(arr))

answer = ''
count = len(arr) - 1
print(reverse)
for i in reversed(range(len(reverse))):
    print(reverse[i],count)
    if reverse[i] == count:
        answer = '{} '.format(nums[i]) + answer
        count -= 1

print(answer)