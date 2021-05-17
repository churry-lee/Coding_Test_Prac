# 리트코드 21. 두 정렬 리스트의 병합
# l1 = [1, 2, 4], l2 = [1, 3, 4]
# return [1, 1, 2, 3, 4, 4]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = result = ListNode(None)
        while l1 and l2:
            # if first node is small, add that to result
            if l1.val < l2.val:
                result.next = l1
                l1 = l1.next
            else:
                # else add the other one
                result.next = l2
                l2 = l2.next
            result = result.next
        # add whatever is left
        result.next = l1 or l2
    
        return temp.next

def ListToLink_l1(list_1): # 입력한 리스트를 연결리스트로 변환
        prev = None

        for li in list_1[::-1]:
            node = ListNode(li)
            node.next = prev
            prev = node
            
        return node

def ListToLink_l2(list_2): # 입력한 리스트를 연결리스트로 변환
        prev = None

        for li in list_2[::-1]:
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

# l1 = ListNode(1)
# l1_2 = ListNode(2)
# l1_3 = ListNode(4)
# l1.next = l1_2
# l1_2.next = l1_3

# l2 = ListNode(1)
# l2_2 = ListNode(3)
# l2_3 = ListNode(4)
# l2.next = l2_2
# l2_2.next = l2_3

list_1 = [1, 2, 4]
list_2 = [1, 3, 4]

solution = Solution()
result = solution.mergeTwoLists(ListToLink_l1(list_1), ListToLink_l2(list_2))
PrintResult(result)
