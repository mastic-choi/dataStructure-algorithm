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