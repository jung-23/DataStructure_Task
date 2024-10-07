from ArrayStack import ArrayStack

map = [['1','1','1','1','1','1','1','1','1','1'],
       ['e','0','0','0','0','0','0','0','0','0'],
       ['1','0','1','0','1','1','1','1','1','1'],
       ['1','1','1','0','1','0','0','0','0','x'],
       ['1','1','1','0','0','0','1','1','1','1'],
       ['1','1','1','1','1','0','1','1','1','1'],
       ['1','1','1','1','1','0','1','1','1','1'],
       ['1','1','1','1','1','0','1','1','1','1'],
       ['1','1','1','1','1','0','1','1','1','1'],
       ['1','1','1','1','1','0','1','1','1','1']]
maze_size = 10

def isValidPos(x, y) :		# (x,y)가 갈 수 있는 방인지 검사하는 함수
    if 0 <= x < maze_size and 0 <= y < maze_size :
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def DFS():
    cnt = 0
    print('DFS: ')
    stack = ArrayStack(100)
    stack.push((1,0,cnt))

    while not stack.isEmpty():
        here=stack.pop()
        print(here,end='->')
        (x,y,cnt)=here

        if (map[y][x]=='x'):
            return True, cnt
        
        else:
            map[y][x]='.'
            if isValidPos(x,y-1):stack.push((x,y-1,cnt + 1))
            if isValidPos(x,y+1):stack.push((x,y+1,cnt + 1))
            if isValidPos(x-1,y):stack.push((x-1,y,cnt + 1))
            if isValidPos(x+1,y):stack.push((x+1,y,cnt + 1))


        print('현재 스택: ',stack)

    return False

result,cnt = DFS()

if result :print('-->미로탐색 성공 (이동거리: %d)'%(cnt))
else: print('--> 미로탐색 실패')