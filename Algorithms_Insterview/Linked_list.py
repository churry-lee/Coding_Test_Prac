# 연결리스트 기본 틀
class ListNode:                     # Node 클래스 선언
    def __init__(self, val):   # 객체 초기화(초기화자)
        self.val = val         # 노드 객체에서 data(or item)을 넣는 변수
        self.next = None        # 노드 객체에서 링크를 나타내는 변수


def ListToLink(input_list): # 입력한 리스트를 연결리스트로 변환
        prev = None

        for li in input_list[::-1]:
            node = ListNode(li)
            node.next = prev
            prev = node
            
        return node

def PrintResult(result):          # 연결리스트 출력
        node = ListToLink(input_list)

        while node:
            print('node: ', node.val, '/', ' node.next: ', node.next.val)
            node = node.next
            if node.next == None:
                print('node: ', node.val)
                break
        return node

# head = ListNode(2)
# node2 = ListNode(4)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
input_list = [1, 2, 3, 4, 5]

PrintResult(input_list)
