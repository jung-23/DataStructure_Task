

# 코드 5.1: 배열로 구현된 원형 큐 클래스
class CircularQueue :
    def __init__( self, capacity = 10 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty() :
            self.front = (self.front + 1) % self.capacity
            self.array[self.front] = None
            return self.array[self.front]
        
        else : self.array = [None] * self.capacity

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]


    # 코드 5.2: 큐의 전체 요소의 수 계산
    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    # 코드 5.3: 문자열 변환을 위한 str 연산자 중복
    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1] )


#======================================================================
if __name__ == "__main__":
    q = CircularQueue(10)

    while True :
        command = input("[메뉴선택] e-enqueue, d-dequeue, q-종료=> ")

        if command == 'e':
            q.enqueue(input("입력: "))

        if command == 'd':
            q.dequeue()

        if command == 'q':
            break
        
        print(q)
