# 런너를 이용한 풀이
class ListNode:
    def __init__(self, item):
        self.data = item
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
       rev = None
       slow = fast = head
       
       while fast and fast.next:
           fast = fast.next.next
           rev, rev.next, slow = slow, rev, slow.next
       if fast:
           slow = slow.next
       
       while rev and rev.data == slow.data:
            slow, rev = slow.next, rev.next
       return not rev

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(1)
head.next = node1
node1.next = node2

solution = Solution()
print(solution.isPalindrome(head))