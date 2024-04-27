#queue problem

# leet code problem link : https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/


#BruteForce Approach
class QueueNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self):
        self.studHead = QueueNode()
        self.studTail = QueueNode()
        self.sandHead = QueueNode()
        self.sandTail = QueueNode()
        self.count = 0
        self.studLength = 0

    def convertListToQueue(self,students: List[int],cur,tail) -> QueueNode:
        i = 0
        while(i<len(students)):
            cur.next = QueueNode(val=students[i])
            i+=1
            cur = cur.next
        return cur

    def deleteFromStart(self,head):
        if(head.next):
            temp = head.next
            head.next = head.next.next
            temp.next = None
            return temp

    def swift(self,head,tail):
        tail.next = self.deleteFromStart(head)
        return tail.next

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        self.studLength = len(students)
        self.studTail = self.convertListToQueue(students,self.studHead,self.studTail)
        self.sandTail = self.convertListToQueue(sandwiches,self.sandHead,self.sandTail)
        sandCur = self.sandHead.next

        while(sandCur and self.count<self.studLength):
            if (sandCur.val == self.studHead.next.val):
                self.count = 0
                self.deleteFromStart(self.studHead)
                self.studLength-=1
                sandCur = sandCur.next
            else:
                self.count+=1
                self.studTail = self.swift(self.studHead,self.studTail)
        return self.studLength


#optimal solution
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0,0]
        for i in students:
            count[i]+=1
        for j in sandwiches:
            if (j == 0 and count[0] ==0):
                return count[1]
            elif (j == 1 and count[1]==0):
                return count[0]
            if (j == 0 ):
                count[0]-=1
            else:
                count[1]-=1
        return 0