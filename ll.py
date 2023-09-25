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

# Introduction To Linked List
def constructLL(arr: [int]) -> Node:
    head=Node(arr[0])
    temp=head
    for i in range(1,len(arr)):
        curr=Node(arr[i])
        temp.next=curr
        temp=temp.next
    return head

# Insert Node At The Beginning
def insertAtFirst(list: Node, newValue: int) -> Node:
    # Write your code here
    new=Node(newValue)
    new.next=list
    return new

# 237. Delete Node in a Linked List(Leetcode)
def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val=node.next.val
    node.next=node.next.next

# Delete Node Of Linked List
def deleteLast(list: Node) -> Node:
    # Write your code here
    temp=list
    while list.next.next!=None:
        list=list.next
    list.next=None
    return temp

# Count nodes of linked list
def length(head) :
    c=0
    while head!=None:
        c+=1
        head=head.next
    return c

# Search in a Linked List
def searchInLinkedList(head, k):
    # Your code goes here.
    while head!=None:
        if k==head.data:
            return 1
        head=head.next
    return 0


