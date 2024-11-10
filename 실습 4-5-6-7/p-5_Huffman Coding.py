import MinHeap

def make_tree(freq):
    heap =[0]
    for n in freq :
        MinHeap.heappush(heap,n)
    for i in range(1,len(freq)):
        e1 = MinHeap.heappop(heap)
        e2 = MinHeap.heappop(heap)
        MinHeap.heappush(heap,e1+e2)
        print("(%d+%d)"%(e1,e2))

while (1) :
    label = input("Please a word: ")
    if label == 'koreatch' :
        label = list(label)
        break
    else : print("illegal character")

freq = [10,5,2,15,18,4,7,11]

print(label)
make_tree(freq)