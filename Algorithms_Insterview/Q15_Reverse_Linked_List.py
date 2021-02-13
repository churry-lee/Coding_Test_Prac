# 리트코드 206
# 주어진 연결리스트를 뒤집어서 출력해라
# 입력: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
# 출력: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
# 이해가 될 듯 하면서도 안됨....

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head     # node(정방향) 초기값
        prev = None     # prev(역방향) 초기값

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev
#               node = 1     node = 2     node = 3     node = 4     node = 5
#             prev = None    prev = 1     prev = 2     prev = 3     prev = 4
# next              2            3            4            5          None
# node.next        None          1            2            3            4
# prev              1            2            3            4            5
# node              2            3            4            5          None
# prev = 5 일 때, node.next = 4
# prev = 4 일 때, node.next = 3 ....  백트래킹 과정을 거치면서 값을 출력한다.

def ListToLink(input_list): # 입력한 리스트를 연결리스트로 변환
        prev = None

        for li in input_list[::-1]:
            node = ListNode(li)
            node.next = prev
            prev = node
            
        return node

def PrintResult(result):              # 결과 연결리스트 출력
    node = result

    while node:
        print('node: ', node.val, '/', ' node.next: ', node.next.val)
        node = node.next
        if node.next == None:
            print('node: ', node.val, '/', ' node.next: ', None)
            break
    
    return node

# head = ListNode(1)
# node_2 = ListNode(2)
# node_3 = ListNode(3)
# node_4 = ListNode(4)
# node_5 = ListNode(5)
# head.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = node_5

input_list = [1, 2, 3, 4, 5]

solution = Solution()
result = solution.reverseList(ListToLink(input_list))
PrintResult(result)