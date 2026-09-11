# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = ListNode(l1[0])
        head2 = ListNode(l2[0])

        curr1 = head1
        curr2 = head2

        for num in l1[1:]:
            curr1.next = ListNode(num)
            curr1 = curr1.next

        for num in l2[1:]:
            curr2.next = ListNode(num)
            curr2 = curr2.next

        def addNum(head1, head2):
            cur1 = head1
            cur2 = head2
            l1Val = ''
            l2val = ''

            while cur1 :
                l1Val += str(cur1.val)
                cur1 = cur1.next

            while cur2 :
                l2val += str(cur2.val)
                cur2 = cur2.next

            l1Val = int(l1Val[::-1])
            l2val = int(l2val[::-1])

            addedNum  = str(l1Val + l2val)
            listRet = [i for i in addedNum[::-1]]

            newHead = ListNode(listRet[0])
            cur = newHead
            for num in listRet[1:]:
                cur.next = ListNode(num)
                cur = cur.next


            return newHead            
                
        def iterate(head):
            cur = head
            while cur :
                print(cur.val, end=" -> ")
                cur = cur.next
            print("Last")

        
        addition = addNum(head1, head2)

        return iterate(addition)

p = Solution()
print(p.addTwoNumbers([1,2,3,5,5,1], [0,1,3]))