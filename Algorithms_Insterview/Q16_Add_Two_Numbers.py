# 리트코드 2
# 역순으로 저장된 연결 리스트의 숫자를 더하라.

# l1 = [2, 4, 3]
# l2 = [5, 6, 4]

# dummy node 관리
# result = ListNode(0)
#       result = 0 -> None
# result_tail = result
#       result_tail = 0 -> None
# result_tail.next = ListNode(1)
#       result_tail = 0 -> 1 -> None
#       result = 0 -> 1 -> None
# result_tail = result_tail.next
#       result_tail = 1 -> None
#       result = 0 -> 1 -> None
# result_tail.next = ListNode(2)
#       result_tail = 1 -> 2 -> None
#       result = 0 -> 1 -> 2 -> None
# result_tail = result_tail.next
#       result_tail = 2 -> None
#       result = 0 -> 1 -> 2 -> None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = l3 = ListNode(0) # answer 변수 없이 실행하면 dummy node로 인해 원하는 결과 못 얻음
                                  # 따라서, answer 변수를 만들어 주어 dummy node를 관리 할 수 있다.
        carry = 0  # 두 수의 합이 10을 넘어갈 때, 10 자리의 수를 저장해줄 변수
        while l1 or l2 or carry:
            l3_sum = 0 # 두 연결리스트의 합을 저장해줄 변수

            if l1:
                l3_sum += l1.val
                l1 = l1.next
            if l2:
                l3_sum += l2.val
                l2 = l2.next

            carry, val = divmod(l3_sum + carry, 10) # 더해진 값이 10을 넘어가는지 판별하기 위해 나머지 연산 사용, 
                                                    # 10이 넘어갈 경우 carry에 1 저장, val에 나머지 저장
            l3.next = ListNode(val)   # 구해진 값을 l3 연결리스트로 만들어줌
            l3 = l3.next

        return answer.next  # l3 로 반환하게 되면 dummy 가 포함되기 때문에 별도의 변수 사용

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

# l1 = ListNode(2)
# l1_2 = ListNode(4)
# l1_3 = ListNode(3)
# l1.next = l1_2
# l1_2.next = l1_3

# l2 = ListNode(5)
# l2_2 = ListNode(6)
# l2_3 = ListNode(4)
# l2.next = l2_2
# l2_2.next = l2_3

list_1 = [2, 4, 3]
list_2 = [5, 6, 4] 

solution = Solution()
result = solution.addTwoNumbers(ListToLink_l1(list_1), ListToLink_l2(list_2))
PrintResult(result)