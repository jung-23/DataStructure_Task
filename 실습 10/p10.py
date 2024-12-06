
# 코드 7.1: 선택 정렬 알고리즘        참고 파일: ch07/basic_sort.py

def selection_sort(A) :
    cnt_cp =0
    cnt_mv =0
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            cnt_cp += 1
            if (A[j]<A[least]) :
                
                least = j
        A[i], A[least] = A[least], A[i]
        cnt_mv += 1
    return data,cnt_cp,cnt_mv    # 배열 항목 교환 

# 코드 7.2: 삽입 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def insertion_sort(A) :
    cnt_cp =0
    cnt_mv =0
    n = len(A)
    for i in range(1, n) :
        cnt_cp += 1
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            cnt_cp += 1
            cnt_mv += 1
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return data,cnt_cp,cnt_mv

# 코드 7.3: 버블 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def bubble_sort(A) :
    cnt_cp =0
    cnt_mv =0
    n = len(A)
    for i in range(n-1, 0, -1) :
        bChanged = False
        for j in range (i) :
            cnt_cp +=1
            if (A[j]>A[j+1]) :
                cnt_mv += 1
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True

        if not bChanged: break;			# 교환이 없으면 종료
    return data,cnt_cp,cnt_mv



# Gap만큼 떨어진 요소들을 삽입 정렬
def sortGapInsertion(A, first, last, gap):
    cnt_cp = 0  # 비교 횟수
    cnt_mv = 0  # 이동 횟수
    for i in range(first + gap, last + 1, gap):
        key = A[i]
        j = i - gap
        while j >= first and key < A[j]:
            cnt_cp += 1  # 비교 횟수 증가
            A[j + gap] = A[j]
            cnt_mv += 1  # 이동 횟수 증가
            j = j - gap
        A[j + gap] = key
        cnt_mv += 1  # key를 제자리에 삽입하는 이동
    return cnt_cp, cnt_mv


# 셸 정렬 알고리즘
def shell_sort(A):
    n = len(A)
    gap = n // 2
    total_cp = 0  # 전체 비교 횟수
    total_mv = 0  # 전체 이동 횟수

    while gap > 0:
        if (gap % 2) == 0:
            gap += 1  # gap이 짝수이면 1을 더함
        for i in range(gap):
            cnt_cp, cnt_mv = sortGapInsertion(A, i, n - 1, gap)
            total_cp += cnt_cp
            total_mv += cnt_mv
    #print('     Gap=', gap, A)  # 중간 과정 출력
        gap = gap // 2

    return total_cp, total_mv, A

        
# 최대힙 삽입 알고리즘
def heappush(heap, n):
    cnt_cp = 0  # 비교 횟수
    cnt_mv = 0  # 이동 횟수
    heap.append(n)  # 맨 마지막 노드로 일단 삽입
    i = len(heap) - 1  # 노드 n의 위치
    while i != 1:  # n이 루트가 아니면 up-heap 진행
        pi = i // 2  # 부모 노드의 위치
        cnt_cp += 1  # 비교 횟수 증가
        if n <= heap[pi]:  # 부모보다 작으면 up-heap 종료
            break
        heap[i] = heap[pi]  # 부모를 끌어내림
        cnt_mv += 1  # 이동 횟수 증가
        i = pi  # i가 부모의 인덱스가 됨
    heap[i] = n  # 마지막 위치에 n 삽입
    cnt_mv += 1  # 이동 횟수 증가
    return cnt_cp, cnt_mv


# 최대힙 삽입 알고리즘 (수정)
def heappush(heap, n):
    cnt_cp = 0  # 비교 횟수
    cnt_mv = 0  # 이동 횟수
    heap.append(n)  # 맨 마지막 노드로 삽입
    cnt_mv += 1  # 이동 횟수 증가
    i = len(heap) - 1  # 노드 n의 위치

    while i != 1:  # 루트가 아니면 up-heap 진행
        pi = i // 2  # 부모 노드의 위치
        cnt_cp += 1  # 비교 횟수 증가
        if n <= heap[pi]:  # 부모보다 작으면 up-heap 종료
            break
        heap[i] = heap[pi]  # 부모를 끌어내림
        cnt_mv += 1  # 이동 횟수 증가
        i = pi  # 부모의 인덱스로 이동
    heap[i] = n  # 마지막 위치에 n 삽입
    cnt_mv += 1  # 이동 횟수 증가
    return cnt_cp, cnt_mv


# 최대힙 삭제 알고리즘 (수정)
def heappop(heap):
    cnt_cp = 0  # 비교 횟수
    cnt_mv = 0  # 이동 횟수
    size = len(heap) - 1  # 노드의 개수
    if size == 0:  # 공백 상태
        return None, cnt_cp, cnt_mv

    root = heap[1]  # 루트 노드
    last = heap[size]  # 마지막 노드
    pi = 1  # 부모 노드의 인덱스
    i = 2  # 자식 노드의 인덱스

    while i <= size:  # 마지막 노드 이전까지
        if i < size and heap[i] < heap[i + 1]:  # 오른쪽 자식이 더 크면
            cnt_cp += 1  # 비교 횟수 증가
            i += 1
        cnt_cp += 1  # 비교 횟수 증가
        if last >= heap[i]:  # 마지막 노드가 더 크면 종료
            break
        heap[pi] = heap[i]  # 자식을 부모로 끌어올림
        cnt_mv += 1  # 이동 횟수 증가
        pi = i  # 부모 인덱스 갱신
        i *= 2  # 자식 인덱스 갱신

    heap[pi] = last  # 마지막 노드를 부모 위치로 이동
    cnt_mv += 1  # 이동 횟수 증가
    heap.pop()  # 마지막 노드 삭제
    return root, cnt_cp, cnt_mv


# 힙 정렬 알고리즘 (수정)
def heapSort1(data):
    heap = [0]
    total_cp = 0  # 전체 비교 횟수
    total_mv = 0  # 전체 이동 횟수

    # 데이터를 힙에 삽입
    for e in data:
        cnt_cp, cnt_mv = heappush(heap, e)
        total_cp += cnt_cp
        total_mv += cnt_mv

    # 데이터를 힙에서 제거하며 정렬
    for i in range(1, len(data) + 1):
        root, cnt_cp, cnt_mv = heappop(heap)
        data[-i] = root
        total_cp += cnt_cp
        total_mv += cnt_mv

    return total_cp, total_mv, data

def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2  # 리스트의 균등 분할
        # 왼쪽 부분 리스트 정렬
        cnt_cp_left, cnt_mv_left, A = merge_sort(A, left, mid)
        # 오른쪽 부분 리스트 정렬
        cnt_cp_right, cnt_mv_right, A = merge_sort(A, mid + 1, right)
        # 병합
        cnt_cp_merge, cnt_mv_merge = merge(A, left, mid, right)

        # 각 단계에서의 비교 및 이동 횟수를 합산하여 반환
        return (
            cnt_cp_left + cnt_cp_right + cnt_cp_merge,
            cnt_mv_left + cnt_mv_right + cnt_mv_merge,
            A,
        )
    return 0, 0, A  # 리스트 크기가 1일 때


def merge(A, left, mid, right):
    cnt_cp = 0  # 비교 횟수
    cnt_mv = 0  # 이동 횟수
    sorted_array = [0] * len(A)  # 임시 배열
    k = left  # 병합된 배열에 대한 인덱스
    i = left
    j = mid + 1

    # 두 서브 배열 비교 및 병합
    while i <= mid and j <= right:
        cnt_cp += 1  # 비교 횟수 증가
        if A[i] <= A[j]:
            cnt_mv += 1  # 데이터 이동 횟수 증가
            sorted_array[k] = A[i]
            i += 1
        else:
            cnt_mv += 1  # 데이터 이동 횟수 증가
            sorted_array[k] = A[j]
            j += 1
        k += 1

    # 왼쪽 서브 배열에 남아 있는 요소 복사
    while i <= mid:
        cnt_mv += 1  # 데이터 이동 횟수 증가
        sorted_array[k] = A[i]
        i += 1
        k += 1

    # 오른쪽 서브 배열에 남아 있는 요소 복사
    while j <= right:
        cnt_mv += 1  # 데이터 이동 횟수 증가
        sorted_array[k] = A[j]
        j += 1
        k += 1

    # 병합된 배열을 원본 배열에 복사
    A[left:right + 1] = sorted_array[left:right + 1]

    # 비교 및 이동 횟수 반환
    return cnt_cp, cnt_mv


# Partition 함수 수정
def partition(A, left, right):
    cnt_cp = 0  # 비교 횟수
    cnt_mv = 0  # 이동 횟수
    low = left + 1
    high = right
    pivot = A[left]  # 피벗 설정

    while True:
        # 피벗보다 큰 값을 찾을 때까지 low 증가
        while low <= right and A[low] <= pivot:
            low += 1
            cnt_cp += 1  # 비교 횟수 증가

        # 피벗보다 작은 값을 찾을 때까지 high 감소
        while high >= left + 1 and A[high] > pivot:
            high -= 1
            cnt_cp += 1  # 비교 횟수 증가

        if low >= high:  # low와 high가 교차하면 종료
            break

        # 선택된 두 레코드 교환
        A[low], A[high] = A[high], A[low]
        cnt_mv += 2  # 이동 횟수 증가 (스왑은 2번 이동)

    # high와 피벗 항목 교환
    A[left], A[high] = A[high], A[left]
    cnt_mv += 2  # 이동 횟수 증가
    return high, cnt_cp, cnt_mv


# 퀵 정렬 함수 수정
def quick_sort(A, left, right):
    cnt_cp = 0  # 비교 횟수
    cnt_mv = 0  # 이동 횟수

    if left < right:  # 정렬 범위가 2개 이상인 경우
        q, partition_cp, partition_mv = partition(A, left, right)  # 좌우로 분할
        cnt_cp += partition_cp
        cnt_mv += partition_mv

        # 왼쪽 부분리스트 정렬
        left_cp, left_mv, A = quick_sort(A, left, q - 1)
        cnt_cp += left_cp
        cnt_mv += left_mv

        # 오른쪽 부분리스트 정렬
        right_cp, right_mv, A = quick_sort(A, q + 1, right)
        cnt_cp += right_cp
        cnt_mv += right_mv

    return cnt_cp, cnt_mv, A

from queue import Queue

# Constants for radix sort
BUCKETS = 10  # Number of buckets (0-9 for decimal numbers)
DIGITS = 2    # Maximum number of digits in the largest number

# Modified radix_sort to track and return comparisons and movements
def radix_sort(A):
    queues = [Queue() for _ in range(BUCKETS)]

    n = len(A)
    factor = 1
    total_cp = 0  # Total comparison count
    total_mv = 0  # Total movement count

    for d in range(DIGITS):
        # Distribute elements into buckets based on the current digit
        for i in range(n):
            bucket_index = (A[i] // factor) % BUCKETS
            queues[bucket_index].put(A[i])
            total_mv += 1  # Movement count for putting into the queue

        # Collect elements back into the array
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                total_mv += 1  # Movement count for getting from the queue
                i += 1

        factor *= 10  # Move to the next digit

    return total_cp, total_mv, A

#5, 8, 1, 3, 4
while(1):
    try: # 사용자로부터 데이터를 입력받아 리스트로 변환
        data = list(map(int, input("\n* Please input a data list : ").split(',')))
        break
    except ValueError:
        print("\nPlease Input Again")
        continue  # 오류 발생 시 루프 처음으로 돌아가 다시 입력받음
    
print ("""\n*************************************************
        * Target Sorting Algorithm List
       
Selection(SEL) / Insertion(INS) / Bubble(BUB)/  Shell(SHE)
    Heap(HEA) / Merge(MER) / Quick(QUI) / Radix(RAD) / Finish(F)
       
*************************************************""")
while(1):
    cnt_mv =0
    cnt_cp =0
    temp_dt = data[:]
    mode = input('\n* Select sorting algorithm : ')

    if mode == 'SEL':        
        temp_dt,cnt_cp,cnt_mv=selection_sort(temp_dt)
    elif mode =='INS':
        temp_dt,cnt_cp,cnt_mv = insertion_sort(temp_dt)
    elif mode =='BUB':
        temp_dt,cnt_cp,cnt_mv = bubble_sort(temp_dt)
    elif mode =='SHE':
        cnt_cp,cnt_mv, temp_dt= shell_sort(temp_dt)
    elif mode =='HEA':
        cnt_cp,cnt_mv,temp_dt = heapSort1(temp_dt)
    elif mode =='MER':
        cnt_cp,cnt_mv, temp_dt = merge_sort(temp_dt, 0, len(temp_dt) - 1)
    elif mode =='QUI':
        cnt_cp,cnt_mv,temp_dt = quick_sort(temp_dt, 0, len(temp_dt) - 1)
    elif mode =='RAD':
        cnt_cp,cnt_mv,temp_dt = radix_sort(temp_dt)
    elif mode =='F':
        break
    else: 
        print('Please Select Again')
        continue

    print('\n>> Sorted: ',temp_dt)
    print('>> Number of Comparisons:',cnt_cp)
    print('>> Number of Data Movements: ',cnt_mv)
