#leet code problem link : https://leetcode.com/problems/design-linked-list/description/
# Brute Force
# class ListNode:
#     def __init__(self, val = None,prev = None, next = None):
#         self.prev = prev
#         self.val = val
#         self.next = next

# class MyLinkedList:

#     def __init__(self):
#         self.head = self.tail = ListNode()
#         self.size = 0
    
#     def get(self, index: int) -> int:
#         if self.head == self.tail or index > self.size - 1:
#             return -1
#         else:
#             i = 0
#             cur = self.head.next
#             while(cur):
#                 if i == index:
#                     return cur.val
#                 cur = cur.next
#                 i+=1
#     def addAtHead(self, val: int) -> None:
#         node = ListNode(val)
#         if self.head == self.tail:
#             self.head.next = self.tail = node
#             node.prev = self.head
#         else:
#             node.next = self.head.next
#             node.prev = self.head
#             self.head.next = node
#         self.size+=1
    
#     def addAtTail(self, val: int) -> None:
#         node = ListNode(val)
#         node.prev = self.tail
#         self.tail.next = node
#         self.tail = node
#         self.size+=1

#     def addAtIndex(self, index: int, val: int) -> None:
#         if (index>self.size):
#             return
#         else:
#             node = ListNode(val)
#             cur = self.head
#             i = -1
#             while(cur):
#                 if(i == index-1):
#                     if(cur==self.tail):
#                         self.tail = node
#                     node.next = cur.next
#                     node.prev = cur
#                     cur.next = node
#                     self.size+=1
#                     return
#                 cur = cur.next
#                 i+=1

#     def deleteAtIndex(self, index: int) -> None:
#         if (index>self.size-1 or index<0 or self.head == self.tail):
#             return
#         else:
#             cur = self.head
#             i = -1
#             while(cur):
#                 if(i == index-1):
#                     if(cur.next == self.tail):
#                         self.tail = cur
#                     cur.next.prev = None
#                     cur.next = cur.next.next
#                 cur = cur.next
#                 i+=1
#             self.size-=1     
    # def getValues(self):
    #     cur = self.head.next
    #     arr = []
    #     while(cur):
    #         arr.append(cur.val)
    #         cur = cur.next
    #     return arr



#------------------------------------------------------------------
#optimal solution using two dummy nodes 

class ListNode:
    def __init__(self, val = None,prev = None, next = None):
        self.prev = prev
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.right.prev = self.left
        self.left.next = self.right
    def get(self, index: int) -> int:
        cur = self.left.next
        while(cur and index>0):
            cur = cur.next
            index-=1
        if(cur and cur!=self.right and index==0):
            return cur.val
        else:
            return -1
    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.left.next
        node.prev = self.left
        self.left.next.prev = self.left.next = node
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = self.right.prev = node
    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while(cur and index>0):
            cur = cur.next 
            index-=1
        if(cur and index == 0):
            node = ListNode(val)
            node.prev = cur.prev
            node.next = cur
            cur.prev.next = cur.prev = node
    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while(cur and index>0):
            cur = cur.next 
            index-=1
        if(cur and index == 0 and cur != self.right):
            cur.next.prev = cur.prev
            cur.prev.next = cur.next


