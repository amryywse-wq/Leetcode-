# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None

        cur = head
        prev = False
        cnt = 0                
        
        while cur and not prev:
            cnt += 1
            if cnt == n :
                prev = head
            elif cnt == n-1 and cur.next.next is None :
                head = head.next
                return head

            cur = cur.next


        while cur and cur.next is not None :


            cur = cur.next
            prev = prev.next

        if n != 1:
            prev.next = prev.next.next


        else :
            prev.next = None
        
        

        return head
                 


num = 100
head = False
if num == 1 :
    head = ListNode(1)

for i in range(1, num):
    if not head :
        head = ListNode(1)
        cur = head
        #print(cur.val)
        cur.next = ListNode(2)
        cur = cur.next
    else :
        #print(cur.val)
        cur.next = ListNode(i+1)
        cur = cur.next


def iterate(head):
    
    cur = head
    while cur :

        print(cur.val)
        cur = cur.next
        
p = Solution()

print((iterate(p.removeNthFromEnd(head, 7))))