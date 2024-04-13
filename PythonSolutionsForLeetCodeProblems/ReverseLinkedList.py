#leet code problem link : https://leetcode.com/problems/reverse-linked-list/

class Solution:
    #Recursion
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if(not head or not head.next):
    #         return head
    #     newHead = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return newHead

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while(cur):
            temp = prev
            prev = cur
            cur = cur.next
            prev.next = temp
        return prev
    