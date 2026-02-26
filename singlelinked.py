class node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class SLL:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start==None
    def start(self,data):
        n=node(data,self.start)
        self.start=n
    def last(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp.next = next
            temp.next=n
        else:
            self.start=n
            