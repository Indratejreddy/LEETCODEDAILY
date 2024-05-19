# leet code problem link : https://leetcode.com/problems/implement-stack-using-queues/

class QueueNode:

    def __init__(self,val=None,prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyStack:

    def __init__(self):
        self.head = QueueNode()
        self.tail = None        

    def push(self, ele: int) -> None:
        if(self.head.next == None):
            self.head.next = self.tail = QueueNode(val=ele)
            self.tail.prev = self.head
        else:
            temp = self.tail
            self.tail.next = QueueNode(val=ele)
            self.tail = self.tail.next
            self.tail.prev = temp

    def pop(self) -> int:
        temp = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        return temp

    def top(self) -> int:
        return self.tail.val
        
    def empty(self) -> bool:
        if(self.head.next == None):
            return True
        return False
