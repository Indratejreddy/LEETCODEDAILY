#double linkedList problem 

# leet code problem link : https://leetcode.com/problems/design-browser-history/description/

class ListNode:
    def __init__(self,url=None,prev=None,next=None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
    
    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url,self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while(steps and self.cur.prev):
            self.cur = self.cur.prev
            steps-=1
        return self.cur.url
        
    def forward(self, steps: int) -> str:
        while(steps and self.cur.next):
            self.cur = self.cur.next
            steps-=1
        return self.cur.url
    


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)