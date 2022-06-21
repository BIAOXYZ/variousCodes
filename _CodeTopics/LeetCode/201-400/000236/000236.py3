# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 《863. 二叉树中所有距离为 K 的结点》 创造的经典解法，充分利用分叉的前缀信息。
        # https://leetcode.cn/submissions/detail/200526742/

        dic = {root:'m'}
        def dfs_and_form_prefic_dic(node, currPrefix):
            if node.left:
                dic[node.left] = currPrefix + 'l'
                dfs_and_form_prefic_dic(node.left, currPrefix + 'l')
            if node.right:
                dic[node.right] = currPrefix + 'r'
                dfs_and_form_prefic_dic(node.right, currPrefix + 'r')
        
        dfs_and_form_prefic_dic(root, 'm')
        sp, sq = dic[p], dic[q]
        
        # 这部分求公共祖先，可以考虑回头也抽象成一个函数
        res = root
        for i in range(min(len(sp), len(sq))):
            if sp[i] == sq[i]:
                if sp[i] == 'l':
                    res = res.left
                elif sp[i] == 'r':
                    res = res.right
                elif sp[i] == 'm':
                    continue
            else:
                break
        return res
        
"""
https://leetcode.cn/submissions/detail/327882995/

执行用时：
88 ms
, 在所有 Python3 提交中击败了
12.99%
的用户
内存消耗：
195.5 MB
, 在所有 Python3 提交中击败了
5.03%
的用户
通过测试用例：
31 / 31
"""
