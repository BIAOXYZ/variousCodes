"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # 真TM生草，跟答案思想是一模一样的，就是TM不对，怎么看也没看出来哪不对了。关键还TM不好单步，关键的关键还TM没时间。

        if not head:
            return head
        
        def flatten_one_level(cur):
            while cur:
                pre = cur
                if not cur.child:
                    cur = cur.next
                else:
                    nextNode = cur.next
                    cur.next = None
                    if nextNode:
                        nextNode.prev = None
                    
                    cur.next = cur.child; cur.child.pre = cur
                    cur.child = None
                    tail = flatten_one_level(cur.next)
                    tail.next = nextNode
                    if nextNode:
                        nextNode.prev = tail
                    cur = nextNode
            return pre
        
        flatten_one_level(head)
        return head
        
"""
https://leetcode-cn.com/submissions/detail/222902407/

6 / 26 个通过测试用例
状态：解答错误

输入：
[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：
The linked list [1,2,3,7,8,11,12,9,10,4,5,6] is not a valid doubly linked list.
预期结果：
[1,2,3,7,8,11,12,9,10,4,5,6]
"""
