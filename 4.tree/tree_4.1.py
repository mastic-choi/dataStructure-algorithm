#이진 트리를 위한 노드 클래스
class BTNode:
    def __init__(self, elem, left = None, right = None):
        self.data = elem
        self.left = left
        self.right = right