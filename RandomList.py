class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    # 复杂链表的复制
    def copyRandomList(self, head):
        """
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
