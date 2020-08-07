# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        def node_equal(p, q):
            if not p and not q: return True
            elif not p or not q: return False
            else:
                if p.val != q.val: return False
                else: return True

        def double_bfs(p, q):
            stack_p, stack_q = [p], [q]
            while stack_p and stack_q:
                curr_p, curr_q = stack_p.pop(0), stack_q.pop(0)
                if not node_equal(curr_p, curr_q):
                    return False
                # 下面的所有这些情况里，当前的curr_p和curr_q都是相等的，所以判断里只判断一个就ok。
                if curr_p == None:
                    continue
                else:
                    stack_p.append(curr_p.left)
                    stack_p.append(curr_p.right)
                    stack_q.append(curr_q.left)
                    stack_q.append(curr_q.right)
            return True

        return double_bfs(p, q)
        
"""
https://leetcode-cn.com/submissions/detail/95766005/

59 / 59 个通过测试用例
状态：通过
执行用时：20 ms
内存消耗：13 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了69.00%的用户
内存消耗：13 MB, 在所有 Python 提交中击败了5.17%的用户
"""
