"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

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
        
        # 上一个提交错就错在不好直接用plain的二分查找，必须用二分查找的变种
        # 那我还不如直接遍历去寻找新节点的插入位置。
        ind = -1
        for i in range(len(vals)):
            right = vals[i]
            if i == 0:
                left = vals[-1]
            else:
                left = vals[i-1]
            if insertVal < min(vals) or insertVal > max(vals):
                if left == max(vals) and right == min(vals):
                    ind = i
                    break
            else:
                if left <= insertVal <= right:
                    ind = i
                    break

        node = Node(insertVal)
        nodes.insert(ind, node)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = nodes[0]
        return head
        
"""
https://leetcode.cn/submissions/detail/326442254/

执行用时：
64 ms
, 在所有 Python3 提交中击败了
5.59%
的用户
内存消耗：
15.7 MB
, 在所有 Python3 提交中击败了
50.32%
的用户
通过测试用例：
106 / 106
"""
