class Node: 
    def __init__(self, url): 
        self.url: str | None = url
        self.next = None 
        self.prev = None

class BrowserHistory: 
    def __init__(self, homepage): 
        self.head = Node(homepage)
        self.tail = self.head 
        self.current = self.head 

    def visit(self, url: str) -> None: 
        new_homepage = Node(url)
        self.current.next = new_homepage 
        new_homepage.prev = self.current 
        self.current = new_homepage 
        self.tail = self.current 
    
    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.next is None:
                break

            self.current = self.current.next

        return self.current.url

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.current.prev is None:
                break

            self.current = self.current.prev

        return self.current.url




    











    