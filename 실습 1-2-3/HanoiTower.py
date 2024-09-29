# 코드 1.6: 하노이의 탑
# n=원판개수/ fr=처음위치 / tmp = 보조기둥 / to=옮길기둥

import time

def hanoi_tower(n, fr, tmp, to) :
    global cnt
    cnt += 1

    if (n == 1) :
        print("원판 1: %s --> %s" % (fr, to))
    else :
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)


# 테스트
cnt = 0

n = int(input())

start=time.time()
hanoi_tower(n, 'A', 'B', 'C')
end=time.time()

print('호출횟수: %d    실행시간: %f'%(cnt,end-start))