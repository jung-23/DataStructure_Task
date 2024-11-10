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
        if Order == 1:
            print(msg, end='')
            inorder(self.root)
            print()
        if Order == 2:
            print(msg, end='')
            preorder(self.root)
            print()
        if Order == 3:
            print(msg, end='')
            postorder(self.root)
            print()



#=========================================================
#   - 이 파일이 직접 실행될 때에는 다음 문장들을 실행함.
#   - 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음.
#=========================================================
# 코드 9.12: 이진탐색트리를 이용한 맵 테스트 프로그램
if __name__ == "__main__":
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
    value= ["삼오", "일팔", "영칠", "이육", "일이", "영삼", "육팔", "이이", "삼영", "구구"]

    map_in = BSTMap()
    map_in.display("[삽입 전] : ")

    print("order 1 : inorder")
    for i in range(len(data)) :
        map_in.insert(data[i],value[i])
        map_in.display(1,"[삽입 %2d] : "%data[i])
    
    map_pre = BSTMap()
    map_pre.display("[삽입 전] : ")

    print("order 2 : preorder")
    for i in range(len(data)) :
        map_pre.insert(data[i],value[i])
        map_pre.display(2,"[삽입 %2d] : "%data[i])

    map_post = BSTMap()
    map_post.display("[삽입 전] : ")
    print("order 3 : postorder")
    for i in range(len(data)) :
        map_post.insert(data[i],value[i])
        map_post.display(3,"[삽입 %2d] : "%data[i])
