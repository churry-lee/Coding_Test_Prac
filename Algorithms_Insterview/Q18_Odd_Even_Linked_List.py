# 리트코드 328
# 연결 리스트를 홀수자리 노드 다음에 짝수자리 노드가 오도록 재구성하라. 공간 복잡도 O(1),
# 시간 복잡도 O(n)에 풀이하라.
class ListNode:                     # Node 클래스 선언
    def __init__(self, val):   # 객체 초기화(초기화자)
        self.val = val         # 노드 객체에서 data(or item)을 넣는 변수
        self.next = None        # 노드 객체에서 링크를 나타내는 변수

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:  # 예외 처리
            return None
        
        odd = head            # 홀수 할당
        even = head.next      # 짝수 할당
        even_head = head.next # 코드가 진행되며 even의 변수가 바뀌기 때문에 짝수의 헤드 값을 별도로 저장

        # 홀수 자리의 수는 홀수 자리의 수끼리, 짝수 자리의 수는 짝수 자리의 수끼리 연결됨
        while even and even.next: # 짝수가 뒤에 오므로 짝수가 있는 동안에 코드 반복
            odd.next, even.next = odd.next.next, even.next.next # 홀수와 짝수에 값 할당
            odd, even = odd.next, even.next # 각각 바뀐 값 할당
            
        odd.next = even_head # 홀수 자리의 수 마지막 값을 짝수 자리의 수 헤드 값과 연결
        return head

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

input_list = [1, 2, 3, 4, 5]

solution = Solution()
result = solution.oddEvenList(ListToLink(input_list))
PrintResult(result)
