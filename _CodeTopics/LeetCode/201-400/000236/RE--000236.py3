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
        for i in range(1, min(len(sp), len(sq) + 1)):
            if sp[i] == sq[i]:
                if sp[i] == 'l':
                    res = res.left
                elif sp[i] == 'r':
                    res = res.right
            else:
                break
        return res
        
"""
https://leetcode.cn/submissions/detail/327882536/

3 / 31 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: string index out of range
    if sp[i] == sq[i]:
Line 29 in lowestCommonAncestor (Solution.py)
    ret = Solution().lowestCommonAncestor(
Line 56 in __helper__ (Solution.py)
    ret = __DriverSolution__().__helper__(
Line 75 in _driver (Solution.py)
    _driver()
Line 87 in <module> (Solution.py)
最后执行的输入：
[1,2]
2
1
"""
