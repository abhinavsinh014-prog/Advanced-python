# class node:
#     def __init__(self,item=None,next=None):
#         self.item = item
#         self.next = next
# class SLL:
#     def __init__(self,start=None):
#         self.start = start

#     def is_empty(self):
#         return self.start==None
    
#     def insert_start(self,data):
#         n=node(data,self.start)
#         self.start=n

#     def last(self,data):
#         n=node(data)
#         if not self.is_empty():
#             temp=self.start
#             while temp.next is not None:
#                 temp.next = next
#             temp.next=n
#         else:
#             self.start=n
#     def search(self,data):
#         temp=self.start   
#         while temp is not None:
#             if temp.item == data:
#                 return temp
#             temp=temp.next
#         return None
#     def insert_after(self,temp,data):
#         if temp is not None:
#             n=node(data,temp.next)
#             temp.next=n
#     def print_list(self):
#         temp = self.start
#         while temp is not None:
#             print(temp.item,end=" ")
#             temp=temp.next
#     def delete_first(self):
#         if self.start is not None:
#             self.start=self.start.next
#     def delete_last(self):
#         if self.start is None:
#             pass
#         elif self.start is None:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next.next is not None:
#                 temp=temp.next
#             temp.next=None
#     def delete_item(self,data):
#         if self.start is None:
#             pass
#         elif self.start.next is None:
#             if self.start.item==data:
#                 self.start=None
#         else:
#             temp=self.start
#             if temp.item==data:
#                 self.start=None
#             else:
#                 while temp.next is None:
#                     if temp.next.item == data:
#                         temp.next=temp.next.next
#                         break
#                     temp=temp.next

# mylist = SLL()
# mylist.last(200)
# mylist.last(30)
# mylist.insert_start(50)
# mylist.insert_after(mylist.search(200),25)
# mylist.print_list()
# print()
# mylist.delete_item(200)
# mylist.print_list()


#question

# Remove loop in Linked List

class node:
    def __init__(self,val):
        self.next = None
        self.val = val

class remove_loop:
        def remove(self,head):
            if head is None and head.next is None:
                return False
            
            slow = head
            fast = head

            while fast and fast.next is not None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast :
                    break
            if(slow!= fast):
                return False

            slow=head

            if slow== fast:

                while fast.next!=slow:

                  fast= fast.next

            