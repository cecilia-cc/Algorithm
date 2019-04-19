class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def oddEvenMerge(self,head):
        head1, head2 = self.devide(head)
        head2 = self.reverse(head2)
        head = self.merge(head1,head2)
        self.printList(head)
        return head

    def devide(self,head):
        p1,p2 = ListNode(0), ListNode(0)
        cur1, cur2 = p1, p2
        count = 1
        while head != None:
            if count %2 != 0:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
            count +=1
        cur1.next = None # !
        cur2.next = None # !
        return p1.next, p2.next

    # LC 206
    def reverse(self,head):
        if head == None:
            return None
        if head.next == None:
            return head
        p, cur , last = head, head, None
        while p.next:
            cur = p
            p = p.next
            cur.next = last
            last = cur
        p.next = last
        return p

    # LC 21
    def merge(self,head1,head2):
        if head1==None: return head2
        if head2==None: return head1
        head = ListNode(0)
        p = head
        while head1 and head2:
            if head1.val <= head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        if head1:
            head.next = head1
        if head2:
            head.next = head2
        return p.next

    def printList(self, head):
        h = head
        val = []
        while h != None:
            val.append(h.val)
            h = h.next
        print(val)

    def oddEvenMerge2(self,head):
        # use array O(nlogn)
        array = []
        while head:
            array.append(head.val)
            head=head.next
        print(array)
        array.sort()
        h = ListNode(0)
        p = h
        for num in array:
            p.next = ListNode(num)
            p = p.next
        self.printList(h.next)
        return h.next


l1 = ListNode(1)
l2 = ListNode(8)
l3 = ListNode(3)
l4 = ListNode(6)
l5 = ListNode(5)
l6 = ListNode(4)
l7 = ListNode(7)
l8 = ListNode(2)
l9 = ListNode(9)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9
l9.next = None

# 1 -> 8 -> 3 -> 6 -> 5 -> 4 -> 7 -> 2 -> 9
# 奇数节点递增 偶数节点递减 排序
# expected 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
s = Solution()
print(s.oddEvenMerge(l1))
#print(s.oddEvenMerge2(l1))