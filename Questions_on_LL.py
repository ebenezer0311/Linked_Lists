# Medium LL Questions
# 876. Middle of the Linked List
class Solution:
    def middleNode(self, head):
        fast,slow=head,head
    
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow

# 206. Reverse Linked List
class Solution:
    def reverseList(self, head):
        if head==None or head.next==None : return head
        def rev(prev ,curr):
            while curr!=None:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
            
        
        prev=None
        curr=head
        
        prev=rev(prev,curr)
        return prev

# 141. Linked List Cycle
class Solution:
    def hasCycle(self, head):
        slow,fast=head,head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
        return False

# 142. Linked List Cycle II
class Solution:
    def detectCycle(self, head):
        slow,meet_pt,fast=head,head,head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                while slow!=meet_pt:
                    slow=slow.next
                    meet_pt=meet_pt.next
                return meet_pt
            
        return None

# Find length of Loop
def lengthOfLoop(head):
    if head==None or head.next==None:
        return None
    
    fast,slow=head,head
    c=0
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            while True:
                c+=1
                fast=fast.next
                if fast==slow:
                    break
            break
        
    return c

# 234. Palindrome Linked List
class Solution:
    def isPalindrome(self, head):
        slow,fast=head,head

        while fast != None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        while slow!=None:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
    
        while prev!=None:
            if head.val!=prev.val:
                return 0
            head=head.next
            prev=prev.next
        return 1

# 328. Odd Even Linked List
class Solution:
    def oddEvenList(self, head):
        if head==None or head.next==None or head.next.next==None:return head

        odd=head
        even=head.next
        even_head=even

        while even!=None and even.next!=None:
            odd.next=odd.next.next
            even.next=even.next.next

            odd=odd.next
            even=even.next

        odd.next=even_head
        return head