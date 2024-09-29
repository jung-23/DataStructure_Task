from ArrayStack import ArrayStack

map = [['1','1','1','1','1','1','1','1','1','1'],
       ['e','0','0','0','0','0','0','0','0','0'],
       ['1','0','1','0','1','1','1','1','1','1'],
       ['1','1','1','0','0','0','0','0','0','x'],
       ['1','1','1','0','1','1','1','1','1','1'],
       ['1','1','1','1','1','1','1','1','1','1'],
       ['1','1','1','1','1','1','1','1','1','1'],
       ['1','1','1','1','1','1','1','1','1','1'],
       ['1','1','1','1','1','1','1','1','1','1']]
maze_size = 10

def isValidPos(x, y):  # (x,y)가 갈 수 있는 방인지 검사하는 함수
    if 0 <= x < maze_size and 0 <= y < maze_size:
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def DFS():
    cnt = 0
    print('DFS: ')
    stack = ArrayStack(100)
    stack.push((0, 1, cnt))  # (x, y, 거리)

    while not stack.isEmpty():
        here = stack.pop()
        (x, y, distance) = here
        print((x, y), end='->')

        if map[y][x] == 'x':
            return True, distance  # 목표 지점에 도달 시 거리 반환

        else:
            map[y][x] = '.'  # 방문 처리
            cnt += 1  # 이동 거리 증가
            
            # 상하좌우 방향 탐색
            if isValidPos(x, y - 1):
                stack.push((x, y - 1, distance + 1))
            if isValidPos(x, y + 1):
                stack.push((x, y + 1, distance + 1))
            if isValidPos(x - 1, y):
                stack.push((x - 1, y, distance + 1))
            if isValidPos(x + 1, y):
                stack.push((x + 1, y, distance + 1))

            print('현재 스택: ', stack)

    return False

result, distance = DFS()

if result:
    print('--> 미로탐색 성공 (이동거리: %d)' % distance)
else:
    print('--> 미로탐색 실패')
