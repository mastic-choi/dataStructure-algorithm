class myQueue:
    def __init__(self, capacity=10):
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.myArray = [None]*self.capacity
    
    def isEmpty(self):
        if self.front == self.rear:
            return True
        else: return False
    '''
    원형 Queue가 Full인 상태에서는 front == rear만으로는 Queue의 공백상태를 확인하기 어려움.
    front가 rear바로 다음에 있으면 포화상태로 정의
    '''
    def isFull(self):
        if self.front == (self.rear+1)%self.capacity:
            return True
        else: return False
    
    def Enque(self, elmt):
        if self.isFull():
            return "OverFlow"
        else:
            self.rear = (self.rear+1)%self.capacity
            self.myArray[self.rear] = elmt

    def deque(self):
        if self.isEmpty():
            return "UnderFlow"
        else:
            '''
            answr = self.myArray[self.front]
            self.myArray[self.front] = None #초기화
            self.front = (self.front+1)%self.capacity
            return answr
            '''
            self.front = (self.front+1)%self.capacity
            return self.myArray[self.front]
    def peek(self):
        if self.isEmpty():
            return "UnderFlow"
        else:
            return self.myArray[(self.front+1)%self.capacity]

    def size(self):
        return (self.rear-self.front+self.capacity)%self.capacity
    
    def display(self, msg):
        print(msg, end="")
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.myArray[i%self.capacity], end =", ")
        print("]")
    
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

    def inorder(self, n):
        #이진 트리의 중위순회(LVR)
        if n is not None:
            self.inorder(n.left)    #순환 호출을 통해 좌측 서브 트리처리
            print(n.data, end =' ')
            self.inorder(n.right)   #순환 호출을 통해 우측 서브 트리처리

    def postorder(self, n):
        if n is not None:
            self.inorder(n.left)    #순환 호출을 통해 좌측 서브 트리처리
            self.inorder(n.right)   #순환 호출을 통해 우측 서브 트리처리
            print(n.data, end =' ')

    def levelorder(self, root):
        queue = myQueue()   #queue의 객체 초기화
        queue.Enque(root)   #최초에 루트 노트만 넣기
        while not queue.isEmpty():
            #큐에서 하나의 노트를 꺼내고, 이 노트가 None이 아니면 처리.
            n = queue.deque()
            if n is not None:
                print(n.data, end= ' ')
                # 마지막으로 이 노드의 좌측, 우측 자식 노드를 큐에 삽입.
                queue.Enque(n.left)
                queue.Enque(n.right)
    
    def count_node(self, n):
        if n is None:
            return 0
        else :
            return self.count_node(n.left) + self.count_node(n.right) + 1