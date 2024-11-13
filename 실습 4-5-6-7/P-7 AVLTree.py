from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전     
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전     
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")



from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)




# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)

# 코드 9.14: AVL 트리의 LL회전     
def rotateLL(A) :
	B = A.left
	A.left = B.right
	B.right = A
	return B

# 코드 9.15: AVL 트리의 RR회전     
def rotateRR(A) :
	B = A.right
	A.right = B.left
	B.left = A
	return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")
        return parent



from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def delete(root,node):
    delete_bst (root, node.key)
    return reBalance (root)


# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]
    # node = [0,1,2,3,4,5,6,7,8,9]

    root = None
    for i in node :
        n = BSTNode(i)
        if root == None :
            root = n
        else :
           root = insert_avl(root, n)

    print("\n***삽입***\nAVL: ", end='')
    levelorder(root)    
    print('\n')

    del_node = [1,2,3,4,10]

    if not del_node :
        print("***삭제***\nMessege: ", end='')
        print('삭제할 것이 없습니다.\n')
    elif len(del_node) > len(node):
        print("***삭제***\nMessege: ", end='')
        print('범위를 벗어났습니다.\n')
    else:
        for i in del_node:
            if i not in node:
                print("***삭제***\nMessege: ", end='')
                print('%s는 없는 노드입니다.\n'%(i))
                exit()
            else:
                n = BSTNode(i)
                root = delete(root, n)
        
        print("***삭제***\nAVL: ", end='')
        levelorder(root)
        print('\n')

    
    print("노드의 개수 =", count_node(root))
    print("단말의 개수 =", count_leaf(root))
    print("트리의 높이 =", calc_height(root))
    print()




    # root = None
    # while(True):
    #     order = input('입력 | [i]-insert [d]-delete [q]-end\n--> ')
    #     if order =='q':
    #         break
    #     elif order =='i':            
    #         num=int(input('노드를 입력하세요 : '))
    #         node = BSTNode(num)
    #         if root == None :
    #             root = node
    #         else :
    #             root = insert_avl(root, node)

    #         print("AVL(%s): "%num, end='')
    #         levelorder(root)
    #         print()

    #     elif order =='d':
            
    #         if root == None :
    #             print('트리가 비어있습니다.')
    #             continue
    #         else :
    #             num=int(input('노드를 입력하세요 : '))
    #             node = BSTNode(num)
    #             root = delete(root, node)

    #         print("AVL(%s): "%num, end='')
    #         levelorder(root)
    #         print()

    #     else:
    #         print('다시 선택하세요')
    #         continue