# 리트코드 24
# 연결리스트를 입력받아 페어 단위로 스왑하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(0)
        prev.next = head

        while head and head.next:
            swap_node = head.next  # head.next가 스왑 되는 대상이 되도록 변수 설정
            head.next = swap_node.next # head의 next 노드가 스왑되는 노드가 스왑되기 전 가리키던 노드가 되도록 설정
            swap_node.next = head  # 스왑되는 노드의 next 노드가 head가 되도록 할당
            
            prev.next = swap_node  # prev의 다음 노드가 스왑된 노드가 되도록 설정

            head = head.next       # 다음 노드들의 스왑을 위해 이동
            prev = prev.next.next  

        return root.next  # head node가 바뀌게 되었으므로 새로이 할당된 변수로 반환

def ListToLink(input_list): # 입력한 리스트를 연결리스트로 변환
        prev = None

        for li in input_list[::-1]:
            node = ListNode(li)
            node.next = prev
            prev = node
            
        return node

def PrintResult(input_list):              # 결과 연결리스트 출력
    node = result

    while node:
        print('node: ', node.val, '/', ' node.next: ', node.next.val)
        node = node.next
        if node.next == None:
            print('node: ', node.val, '/', ' node.next: ', None)
            break    
    return node
        
# head = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# head.next = node2
# node2.next = node3
# node3.next = node4
input_list = [1, 2, 3, 4]

solution = Solution()
result = solution.swapPairs(ListToLink(input_list))
PrintResult(result)