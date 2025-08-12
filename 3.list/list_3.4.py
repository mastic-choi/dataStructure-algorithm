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