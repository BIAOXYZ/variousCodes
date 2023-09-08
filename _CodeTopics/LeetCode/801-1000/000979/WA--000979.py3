# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:

        # 首先统计一下以每个节点为根的子树下一共有多少个节点
        dicSum = {}
        def dfs_and_sum(node):
            if not node:
                return 0
            if node in dicSum:
                return dicSum[node]
            sumVal = 1 + dfs_and_sum(node.left) + dfs_and_sum(node.right)
            dicSum[node] = sumVal
            return sumVal
        dfs_and_sum(root)
        
        # 然后自底向上开始，每个子节点计算自己当前有多少值（或者说能给以自己为根的子树提供多少个节点）
        # currNodesCanProvide 和实际的sum 差一个 diff，这个 diff 会由自己的父节点来补，且由于是
        ## 父节点，差了 diff 个节点（不管正还是负），都只需要 abs(diff) 次移动即可。
        ## 最终一直到根节点，根节点不需要再统计了（肯定是从其他地方调节好了），所以根节点的 abs(diff) 不会加到res里。
        res = 0
        def dfs_and_count_move(node):
            if not node:
                return 0
            nonlocal res
            currNodesCanProvide = node.val + dfs_and_count_move(node.left) + dfs_and_count_move(node.right)
            diff = currNodesCanProvide - dicSum[node]
            if node != root:
                res += abs(diff)
            return diff
        dfs_and_count_move(root)
        return res
        
"""
https://leetcode.cn/problems/distribute-coins-in-binary-tree/submissions/464392943/

解答错误
13 / 148 个通过的测试用例

输入
[1,0,0,null,3]

输出
3
预期结果
4
"""
