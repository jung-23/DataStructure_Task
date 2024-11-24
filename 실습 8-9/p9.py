# Floyd 알고리즘
INF = 9999
def shortest_path_floyd(vertex, adj, start, end):
    vsize = len(vertex)
    A = list(adj) # 인접 행렬 복사
    path = [[i if adj[i][j] != INF else -1 for j in range(vsize)] for i in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = path[k][j]

    # 최단 경로 구성
    if path[start][end] == -1:
        route = "경로 없음"
    else:
        route = []
        current = end
        while current != start:
            route.append(vertex[current])
            current = path[start][current]
        route.append(vertex[start])
        route = ' -> '.join(reversed(route))

    return A[start][end], route

if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0]
    ]

    start = input('Start Vertex를 입력하세요: ')
    end = input('End Vertex를 입력하세요: ')

    if start in vertex and end in vertex:
        start_idx = vertex.index(start)
        end_idx = vertex.index(end)

        distance, route = shortest_path_floyd(vertex, weight, start_idx, end_idx)
        print('Shortest path: %s' % route)
        print('Distance of the Shortest path: %s' % distance)
    else:
        print('잘못된 입력입니다. 올바른 정점을 입력하세요.')
