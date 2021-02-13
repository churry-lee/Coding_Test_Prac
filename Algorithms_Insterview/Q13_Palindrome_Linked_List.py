# 리트코드 234
# 연결 리스트 문제
# 개념 겁나 어려운데 자료구조 알고리즘 가장 기초라고 함

class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        
        if not head:             # head 가 없을 경우 True 출력
            return True
        
        node = head
        while node is not None:     # node가 비어있지 않을 경우, node의 데이터 값들을 q 리스트에 추가
            q.append(node.data)
            node = node.next
            
        while len(q) > 1:           # 생성된 q 리스트의 길이가 1 보다 클 경우 실행
            if q.pop(0) != q.pop(): # 제일 앞과 제일 뒤의 값을 비교, 만약 두 값이 다를 경우 False 출력
                return False
            
        return True

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(1)
head.next = node1
node1.next = node2

solution = Solution()
print(solution.isPalindrome(head))