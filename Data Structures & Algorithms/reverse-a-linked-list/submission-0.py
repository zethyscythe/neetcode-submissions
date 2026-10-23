# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 ->1
        #pointer=head
        #head.next=None

        curr=head
        prev=None


        while curr:
            #temp=1->2
            temp=curr.next
            #curr=0->None
            curr.next=prev
            #prev=0->None
            prev=curr
            #curr=2->3
            curr=temp

        #return prev    
        return prev

          


        