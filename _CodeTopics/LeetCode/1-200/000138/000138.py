"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return None
        
        nodeList, nodeDic = [head], {head:0}
        curr, currInd = head.next, 1
        while curr:
            nodeList.append(curr)
            nodeDic[curr] = currInd
            curr = curr.next
            currInd += 1
        indexListForRandom = []
        for node in nodeList:
            if not node.random:
                indexListForRandom.append(-1)
            else:
                indexListForRandom.append(nodeDic[node.random])

        # 又是一个列表推导式问题的例子：这里如果用 nodeList2 = [Node(0)] * currInd 就不行！
        nodeList2 = [Node(0) for _ in range(currInd)]
        for i in range(currInd):
            nodeList2[i].val = nodeList[i].val
            if i == currInd - 1:
                nodeList2[i].next = None
            else:
                nodeList2[i].next = nodeList2[i+1]
            if indexListForRandom[i] != -1:
                nodeList2[i].random = nodeList2[indexListForRandom[i]]
            else:
                nodeList2[i].random = None
        return nodeList2[0]
        
"""
https://leetcode-cn.com/submissions/detail/198402424/

19 / 19 个通过测试用例
状态：通过
执行用时: 32 ms
内存消耗: 13.8 MB

执行用时：32 ms, 在所有 Python 提交中击败了99.20%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了44.62%的用户
"""
