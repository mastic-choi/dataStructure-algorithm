#Node 클래스 구현 후, 이를 이횽한 단순 연결 리스트 클래스를 생성
class Node:
    def __init__ (self, elem, link = None):
        self.data = elem
        self.link = link

    def append(self, node): #self라는 노드 뒤에 node를 넣는 연산
        if node is not None:
            node.link = self.link #node의 링크가 self.link를 가르키게 함
            self.link = node      #self의 링크가 node를 가리키게 함

    def popNext(self):
        next = self.link
        if next is not Node:
            self.link = next.link
        return next

class linkedList(Node):
    #단순 연결 리스트 클래스 구현, Node Class를 부모클래스로 받아 활용한다.
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def isFull(self):
        return False
    
    def getNode(self, pos):
        #POS번째 요소를 찾는 함수
        if pos<0: return None   #시작 위치 -> Head에서 시작
        ptr = self.head         #시작 위치 -> Head에서 시작
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr
    
    def getEntry(self, pos):
        #POS번째 요소를 반환하는 함수
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
        
    def insert(self, pos, e):
        #Pos 위치에 새로운 요소를 삽입하는 insert연산
        node = Node(e, None)            #삽입할 새로운 노드를 만듦
        before = self.getNode(pos - 1)  #삽입할 위치 이전 노드 탐색
        if before == None:
            node.link = self.head
            self.head = node
        else:
            before.append(node)
    def delet(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before == self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        else:
            return before.popNext()
        
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:  #ptr이 None이 아닌동안
            ptr = ptr.link      #링크를 따라 Ptr을 찾음
            count += 1          #이동거리를 계산ㄴ
        return count
    def display(self, msg='LinkedList : '):
        print(msg, end = '')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '->')
            ptr = ptr.link
        print('None')