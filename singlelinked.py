class node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class SLL:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start==None
    
    def insert_start(self,data):
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
    def search(self,data):
        temp=self.start   
        while temp is not None:
            if temp.item == data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=",")
            temp=temp.next
    
mylist = SLL()
mylist.insert_start(20)
mylist.last(30)
mylist.insert_start(10)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
print()