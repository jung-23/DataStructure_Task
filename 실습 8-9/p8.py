# A, B, C, D, E, F, G, H
# A-B, A-C, B-D, C-D, C-E, D-F, E-H, E-G, G-H

# vertext 입력
vtx=input('\nvertext를 입력하세요: ').split(', ')
# edge 입력
edge_in = input('edge \'-\'이용하여 입력하세요: ').split(', ')
# 리스트 출력
print('\n'+
      '*'*37,
      '\nVertex List: ',vtx,'\nAdjacent List: ',edge_in,'\n')

# edge 정리
edge = [[0]* len(vtx) for _ in range(len(vtx))]
for i in edge_in:
    edge[vtx.index(i[0])][vtx.index(i[2])] = 1
    edge[vtx.index(i[2])][vtx.index(i[0])] = 1


#adjacent vertext 리스트
adjacency_dict = {v: [] for v in vtx}
for n in edge_in:
    start, end = n.split('-')
    adjacency_dict[start].append(end)
    adjacency_dict[end].append(start)
for key in adjacency_dict: # 알파벳 순서로 정렬
    adjacency_dict[key].sort()

print ('*'*7,'Adjacent Vertext List','*'*7) # 출력
for v, s in adjacency_dict.items():
    print(f"{v}: {s}")


# DFS
def DFS(vtx, adj, s, visited,ouput) :
    output.append(vtx[s])       # 현재 정점 s를 출력함
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                DFS(vtx, adj, v, visited,output)
#DFS 출력
print('\n'+'*'*37,'\nDFS: ',end='')
output=[]
DFS(vtx, edge, 0, [False]*len(vtx),output)
print('-'.join(output))

#BFS
from queue import Queue                 # queue 모듈의 Queue 사용
def BFS_AL(vtx, aList, s):
    n = len(vtx)                        # 그래프의 정점 수
    visited = [False]*n                 # 방문 확인을 위한 리스트
    Q = Queue()                         # 공백상태의 큐 생성
    Q.put(s)                            # 맨 처음에는 시작 정점만 있음
    visited[s] = True                   # s는 "방문"했다고 표시
    output=[]
    while not Q.empty() :
        s = Q.get()                     # 큐에서 정점을 꺼냄
        output.append(vtx[s])        # 정점을 출력(처리)함
        for v in aList[s] :               # s의 모든 이웃 v에 대해
            if visited[v]==False :      # 방문하지 않은 이웃 정점이면
                Q.put(v)                # 큐에 삽입
                visited[v] = True
    return output  
#aList 생성
aList=[]
for key in vtx:
    neighbors = [vtx.index(neighbor) for neighbor in adjacency_dict[key]]
    aList.append(neighbors)

#BFS 출력
print('BFS: ',end='')
output = BFS_AL(vtx, aList, 0)
print('-'.join(output))


# connected component
def find_connected_component(vtx, adj) :
    n = len(vtx)
    visited = [False]*n
    groups = []		# 부분 그래프별 정점 리스트

    for v in range(n) :
        if visited[v] == False :
            color = bfs_cc(vtx, adj, v, visited)
            groups.append( color )

    return groups

def bfs_cc(vtx, adj, s, visited):
    group = [s]    # 새로운 연결된 그룹 생성
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty() :
        s = Q.get()
        for v in range(len(vtx)) :
            if visited[v]==False and adj[s][v] != 0 :
                Q.put(v)
                visited[v] = True
                group.append(v)
    return group

colorGroup = find_connected_component(vtx, edge)
print('\n'+'*'*7,'Connected Component', '*'*7)
print("연결성분 개수 = %d " % len(colorGroup))
print(colorGroup)	# 정점 리스트들을 출력


# spanning tree
def ST_DFS(vtx, adj, s, visited) :
    visited[s] = True               # 현재 정점 s를 visited에 추가함
    for v in range(len(vtx)) :      # 인접행렬
        if adj[s][v] != 0 :         # 모든 간선 (s,v)에 대해
            if visited[v]==False:   # v를 아직 방문하지 않았으면 
                print("(", vtx[s], vtx[v], ")", end=' ')  # 간선 출력
                ST_DFS(vtx, adj, v, visited)

print('\n'+'*'*7,'Spanning Tree','*'*7)
print('신장트리(DFS): ', end="")
ST_DFS(vtx, edge, 0, [False]*len(vtx))
print()