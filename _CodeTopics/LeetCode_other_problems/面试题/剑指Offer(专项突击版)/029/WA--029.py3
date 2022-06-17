"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

import bisect
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        nodes = []
        vals = []
        cur = head
        # 之所以加上 not nodes 是为了能够特殊处理只有一个 node 的情况。
        while not nodes or cur != head:
            nxt = cur.next
            cur.next = None
            nodes.append(cur)
            vals.append(cur.val)
            cur = nxt
        
        ind = bisect.bisect_right(vals, insertVal)
        node = Node(insertVal)
        nodes.insert(ind, node)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = nodes[0]
        return head
        
"""
https://leetcode.cn/submissions/detail/326440791/

72 / 106 个通过测试用例
状态：解答错误

输入：
[3,5,1]
0
输出：
[3,5,1,0]
预期结果：
[3,5,0,1]
"""
