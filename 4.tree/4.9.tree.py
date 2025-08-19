#MorseCode 구현하기
#찍턴 휴가... 힘들구만~
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
        
    def calc_height(self, n):
        if n is None:
            return 0
        hLeft = self.calc_height(n.left)
        hRight = self.calc_height(n.right)
        if hLeft > hRight:
            return hLeft + 1
        else:
            return hRight + 1


table = [
    ('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'),
    ('F', '..-.'), ('G', '--.'), ('H', '....'), ('I', '..'), ('J', '.---'),
    ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'),
    ('P', '.--.'), ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
    ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'), ('Y', '-.--'),
    ('Z', '--..')]

def encode(ch):
    #문자를 모스코드를 변환하는 인코딩 과정
    #A의 모스코드는 table[0][1], C의 모스코드는 table[2][1]
    idx = ord(ch) - ord('A')
    return table[idx][1]

def decode_simple(morse):
    #모스 코드를 해당하는 알파벳으로 추출
    for tp in table:
        if morse == tp[1]:  #tp는  ('A', '.-'), tp[1]은 '.-'
            return tp[0]    #표의 크기(문자의 수)가 n개라면 n번 비교해야함(비효율적)

def make_morse_tree():
    #tree_4.9_decision_tree.jpg 속 결정트리를 구현
    root = BTNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root         #루트부터 탐색
        for c in code:
            #C는 chr단위로 입력('.' or '-')
            if c == '.':
                if node.left == None:
                    #좌측 자식 노드가 비었다면, 빈 노드를 추가
                    node.left = BTNode(None, None, None)
                node = node.left #좌측 자식으로 지정
            elif c == '-':
                if node.right == None:
                    #우측 자식 노드가 비었다면, 빈 노드를 추가
                    node.right = BTNode(None, None, None)
                node = node.right #우측측 자식으로 지정
        node.data = tp[0]      
    return root    

def decode(root, code):
    #결정 트리를 이용한 디코딩 함수
    #시간 복잡도는 log_2(N)
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right
    return node.data

morseCodeTree = make_morse_tree()
str = input("문장을 입력하세요 : ")
mList = []
for ch in str:
    code = encode(ch)
    mList.append(code)
print("Morse Code : ", mList)
print("Decoding : ", end = '')
for code in mList:
    ch = decode(morseCodeTree, code)
    print(ch, end ='')
print()
'''
Python Version : 3.13.5
문장을 입력하세요 :  GAMEOVER
Morse Code :  ['--.', '.-', '--', '.', '---', '...-', '.', '.-.']
Decoding : GAMEOVER
'''