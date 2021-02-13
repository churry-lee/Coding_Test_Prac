# 리트코드 92
# 인덱스 m에서 n까지를 역순으로 만들어라.
# 인덱스 m은 1부터 시작한다.

class ListNode:                     # Node 클래스 선언
    def __init__(self, val):   # 객체 초기화(초기화자)
        self.val = val         # 노드 객체에서 data(or item)을 넣는 변수
        self.next = None        # 노드 객체에서 링크를 나타내는 변수

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 예외처리
        if not head or m == n:
            return head

        root = start = ListNode(None)
        root.next = head
        # start node 지정
        for _ in range(m-1):
            start = start.next
        end = start.next  # end node 지정
        # 반복문을 거쳐 node를 뒤집기
        for _ in range(n-m):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

#          |  start   end  |  tmp   start.next   end.next   start.next.next
#  for 1   |    1      2   |   2        3           4              2           1 -> 3 -> 2 -> 4 -> 5
#  for 2   |    1      2   |   3        4           5              3           1 -> 4 -> 3 -> 2 -> 5

        return root.next

def ListToLink(input_list): # 입력한 리스트를 연결리스트로 변환
        prev = None

        for li in input_list[::-1]:
            node = ListNode(li)
            node.next = prev
            prev = node
            
        return node

def PrintResult(result):          # 연결리스트 출력
        node = result

        while node:
            print('node: ', node.val, '/', ' node.next: ', node.next.val)
            node = node.next
            if node.next == None:
                print('node: ', node.val, '/', ' node.next: ', None)
                break
        return node

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
m = 4
n = 10

solution = Solution()
result = solution.reverseBetween(ListToLink(input_list), m, n)
PrintResult(result)