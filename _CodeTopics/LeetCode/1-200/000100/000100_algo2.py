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
        
        def return_all_nodes_bfs(node):
            if not node:
                return []
            temp, res = [node], [node.val]
            while temp:
                currnode = temp.pop(0)
                if currnode == None:
                    continue
                if currnode.left == currnode.right == None:
                    continue
                elif currnode.left and not currnode.right:
                    temp.append(currnode.left)
                    temp.append(None)
                    res.append(currnode.left.val)
                    res.append(None)
                elif currnode.right and not currnode.left:
                    temp.append(None)
                    temp.append(currnode.right)
                    res.append(None)
                    res.append(currnode.right.val)
                else:
                    temp.append(currnode.left)
                    temp.append(currnode.right)
                    res.append(currnode.left.val)
                    res.append(currnode.right.val)
            if res[-1] == None:
                res.pop()
            return res

        return return_all_nodes_bfs(p) == return_all_nodes_bfs(q)
        
"""
https://leetcode-cn.com/submissions/detail/95758307/

59 / 59 个通过测试用例
状态：通过
执行用时：24 ms
内存消耗：12.7 MB
"""
"""
执行用时：24 ms, 在所有 Python 提交中击败了41.93%的用户
内存消耗：12.7 MB, 在所有 Python 提交中击败了62.93%的用户
"""
