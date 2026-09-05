class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):

    def deleteMiddle(self, head):

        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head




            

        
            
        
        
        



head = ListNode(2)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(9)

p = Solution()
removeMiddle = p.deleteMiddle(head)

while removeMiddle is not None:
    print(removeMiddle.val)
    removeMiddle = removeMiddle.next

