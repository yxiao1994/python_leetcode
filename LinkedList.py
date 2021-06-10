# coding:utf-8
#
# Copyright 2019 Tencent Inc.
# Author: Yang Xiao(mlhustxiao@tecent.com)
#


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def createList(self, input_list):
        dummy = ListNode(0)
        curr = dummy
        for item in input_list:
            curr.next = ListNode(item)
            curr = curr.next
        return dummy.next

    def printList(self, head):
        """
        打印链表
        :param head:
        :return:
        """
        curr = head
        while curr:
            print(curr.val, end='>>>')
            curr = curr.next
        print('end')

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        p1 = l1
        p2 = l2
        sum = 0
        while p1 or p2:
            val1 = 0 if p1 is None else p1.val
            val2 = 0 if p2 is None else p2.val
            sum += (val1 + val2)
            curr.next = ListNode(sum % 10)
            sum //= 10
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            curr = curr.next
        if sum > 0:
            curr.next = ListNode(sum)
        return dummy.next

    def removeNthFromEnd(self, head, n):
        """
        删除倒数第n节点
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pfast = dummy
        pslow = dummy
        for i in range(n + 1):
            if pfast:
                pfast = pfast.next
        while pfast:
            pfast = pfast.next
            pslow = pslow.next
        pslow.next = pslow.next.next
        return dummy.next

    def mergeTwoLists(self, l1, l2):
        """
        合并两个有序链表
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2:
            if not l1:
                curr.next = l2
                return dummy.next
            elif not l2:
                curr.next = l1
                return dummy.next
            else:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
        return dummy.next

    def deleteNode(self, head, val):
        """
        删除链表中值等于val的节点
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pfast, pslow = dummy.next, dummy
        while pfast and pfast.val != val:
            pfast = pfast.next
            pslow = pslow.next
        pslow.next = pfast.next
        return dummy.next

    def reverseList(self, head):
        """
        链表反转
        :type head: ListNode
        :rtype: ListNode
        """
        p_curr = head
        p_before = None
        while p_curr:
            p_next = p_curr.next
            p_curr.next = p_before
            p_before = p_curr
            p_curr = p_next
        return p_before

    def reverseBetween(self, head, m, n):
        """
        反转从位置 m 到 n 的链表
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        phead = dummy
        for i in range(m - 1):
            phead = phead.next
        pbefore = None
        pcurr = phead.next
        for i in range(m, n + 1):
            pnext = pcurr.next
            pcurr.next = pbefore
            pbefore = pcurr
            pcurr = pnext
        phead.next.next = pcurr
        phead.next = pbefore
        return dummy.next

    def copyRandomList(self, head):
        """
        复杂链表的复制
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        point_dic = {}
        pcurr = head
        new_node = Node(head.val)
        pnew = new_node
        point_dic[head] = new_node

        while pcurr:
            pnext = pcurr.next
            if pnext:
                if pnext not in point_dic:
                    node = Node(pnext.val)
                    point_dic[pnext] = node
                    pnew.next = node
                else:
                    pnew.next = point_dic[pnext]

            prandom = pcurr.random
            if prandom:
                if prandom not in point_dic:
                    node = Node(prandom.val)
                    point_dic[prandom] = node
                    pnew.random = node
                else:
                    pnew.random = point_dic[prandom]

            pcurr = pnext
            pnew = pnew.next

        return new_node

    def hasCycle(self, head):
        """
        链表是否有环
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        pfast = head.next
        pslow = head
        while pslow != pfast:
            if not pfast or not pfast.next:
                return False
            pfast = pfast.next.next
            pslow = pslow.next
        return True

    def sortList(self, head):
        """
        链表排序
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pfast, pslow = head.next, head
        while pfast and pfast.next:
            pfast = pfast.next.next
            pslow = pslow.next
        pright = self.sortList(pslow.next)
        pslow.next = None
        pleft = self.sortList(head)
        return self.mergeTwoLists(pleft, pright)

    def partition(self, head, x):
        """
        对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        pcurr = head
        while pcurr:
            if pcurr.val < x:
                before.next = pcurr
                before = pcurr
            else:
                after.next = pcurr
                after = pcurr
            pcurr = pcurr.next
        before.next = after_head.next
        after.next = None
        return before_head.next

    def reorderList(self, head):
        # 重排链表
        # write your code here
        if not head or not head.next:
            return
        vec = []
        pcurr = head
        while pcurr:
            vec.append(pcurr)
            pcurr = pcurr.next
        i, j = 0, len(vec) - 1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None

    def getIntersectionNode(self, headA, headB):
        """
        两个单链表相交的起始节点
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


if __name__ == "__main__":
    obj = Solution()
    l1 = obj.createList([2, 4, 3])
    l2 = obj.createList([5, 6, 4])
    obj.printList(obj.addTwoNumbers(l1, l2))