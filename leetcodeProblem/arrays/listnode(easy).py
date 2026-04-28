class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

arr = [1,1,2,2,3,3,3,4]


head = ListNode(arr[0])
cur = head
for valP in arr[1:] :
    cur.next = ListNode(valP)
    cur = cur.next
         
def check_list(head):
    cur = head
    while cur :
        print(cur.val, end=" -> ")
        cur = cur.next
    print("Last")

def erase_dup(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else :
            cur = cur.next
    return head
new_list = erase_dup(head)
check_list(new_list)