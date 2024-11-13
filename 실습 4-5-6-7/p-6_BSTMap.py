from BinSrchTree import *

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')   # node의 key만 중위순회로 출력
        inorder(n.right)

def postorder(n) :
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.key,end=' ')

def preorder(n):
    if n is not None:
        print(n.key, end=' ')
        preorder(n.left)
        preorder(n.right)

# 코드 9.11: 이진탐색트리를 이용한 맵 클래스
class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty (self):
       return self.root == None

    def findMax(self):
       return search_max_bst(self.root)

    def findMin(self):
       return search_min_bst(self.root)

    def search(self, key):
       return search_bst(self.root, key)
       #return search_bst_iter(self.root, key)

    def searchValue(self, key):
       return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty() :
           self.root = n
        else :
           insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst (self.root, key)

    def display(self, Order , msg = 'BTSMap :'):
        print(msg, end='')
        if Order == 1:
            inorder(self.root)
        if Order == 2:
            preorder(self.root)
        if Order == 3:
            postorder(self.root)
        print()


if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    text = ['inorder','preorder','postorder']

    while(True):
        print('*'*50)
        order = input("[1]inorder [2]preorder [3]postorder [4]end\n-->")

        if order == '4':
            break
        elif int(order)>=5:
            #print('*'*50)
            print('\nMessege:선택지에서 다시 골라주세요')
            continue

        map_in = BSTMap()
        print("\norder %s : %s"%(order,text[int(order)-1]))
        for i in range(len(data)) :
            map_in.insert(data[i])
            map_in.display(int(order),"[삽입 %2d] : "%data[i])
        print()
