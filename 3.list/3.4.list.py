#이중 연결 구조로 리스트 구현하기
class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem #노드의 데이터
        self.next = next #다음 노드의 링크
        self.prev = prev #이전 노드의 링크
    
    def append(self, node): #self다음에 node를 넣는 연산
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:   #append하기 전, self뒤에 값이 존대한다면,
                node.next.prev = node   #append하기 전, self뒤에 값의 이전은 node(새로 넣으려고 하는 노드)이다.
            self.next = node

    def popNext(self):
        node = self.next #꺼낼 노드 지정
        if node is not None:
            self.next = node.next
            if self.next is not None:
                node.next.prev = self
            return node
        

#이중 연결 리스트 클래스 정의
class DbLinkedList:
    def __init__(self):
        self.head = None

    def display(self, msg = 'DbLinkedList : '):
        print(msg, end = '')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = ' <=> ')
            ptr = ptr.next
        print('None')
    def getNode(self, pos):
        if pos<0: return None   #시작 위치 -> Head에서 시작
        ptr = self.head         #시작 위치 -> Head에서 시작
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr

    def insert(self, pos, e):
            node = DNode(e, None)            #삽입할 새로운 노드를 만듦
            before = self.getNode(pos - 1)  #삽입할 위치 이전 노드 탐색
            if before == None:
                node.next = self.head
                if node.next is not None:
                    node.next.prev = node
                self.head = node
            else:
                before.append(node)
    def delet(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            before == self.head
            if self.head is not None:
                self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return before
        else:
            return before.popNext()