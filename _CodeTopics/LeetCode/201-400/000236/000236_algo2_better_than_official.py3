# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 对每一个节点 node，遍历完会返回一个二元组。
        # 第一个元素表示 p 是否包含在 node 为根结点的子树中；
        # 第二个元素表示 q 是否包含在 node 为根结点的子树中。
        # 于是第一个为 (True, True) 的 node 就是答案。

        res = []
        def dfs(node):
            if not node:
                return (False, False)
            cur = (node == p, node == q)
            left, right = dfs(node.left), dfs(node.right)
            ## print(node.val, cur, left, right)
            # Python3 真是屁事多，下面这个不行，计算结果打印了下是 generator；
            # 加个 bool 强转也不对，先替换成比较龊的写法，早点写完赶紧睡了，艹。
            # cur = (cur[i] or left[i] or right[i] for i in range(2))
            cur = (cur[0] or left[0] or right[0], cur[1] or left[1] or right[1])
            if cur == (True, True) and not res:
                res.append(node)
            return cur
        
        dfs(root)
        return res[0]
        
"""
https://leetcode.cn/submissions/detail/328661205/

执行用时：
68 ms
, 在所有 Python3 提交中击败了
74.05%
的用户
内存消耗：
27.6 MB
, 在所有 Python3 提交中击败了
9.03%
的用户
通过测试用例：
31 / 31
"""
