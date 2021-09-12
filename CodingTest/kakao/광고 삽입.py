def solution(play_time, adv_time, logs):
    print(play_time,adv_time)
    arr=list(map(int,play_time.split(":")))
    print(arr[0])

    answer = ''
    return answer
def divide(a):
    a.split('-')
    return a
def cal(a,b):
    c=[0,0,0]
    i = map(int, a.split(":"))
    b=map(int,b.split(":"))
    print(i)

    if c[2]<0:
        a[1]-=1
    c[1]=a[1]-b[1]+60
    if c[1]<0:
        a[0]-=1
    c[0]=a[0]-b[0]
    return c




if __name__ == '__main__':
    solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])

