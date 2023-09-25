# Basic Append & Prepend
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
        
    def print_val(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
    
    def append(self,data):
        node=Node(data)

        if self.head is None:
            self.head=node
            return 
        
        last=self.head
        while last.next:
            last=last.next
        last.next=node
    
    def prepend(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return 
        
        node.next=self.head
        self.head=node
       
ll=LL()
ll.append(1)
ll.append(4)
ll.append(3)
ll.append(2)
ll.prepend(10)
ll.print_val()
