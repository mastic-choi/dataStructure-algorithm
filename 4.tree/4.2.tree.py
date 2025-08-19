#이진 트리의 전위순회(VLR)
class BTNode:
    def __init__(self, elem, left = None, right = None):
        self.data = elem
        self.left = left
        self.right = right

    def preorder(self, n):
        #이진 트리의 전위순회(VLR)
        if n is not None:
            print(n.data, end =' ')
            self.preorder(n.left)  #순환 호출을 통해 좌측 트리처리
            self.preorder(n.right) #순환 호출을 통해 우측 트리처리
