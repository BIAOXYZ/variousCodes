# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def is_leaf(node):
            return True if not node.left and not node.right else False
        def backtrack_dfs(node, currArr, currSum):
            currSum += node.val
            currArr.append(node.val)
            print "111", currArr
            if is_leaf(node):
                if currSum == sum:
                    res.append(currArr[:])
                return
            if node.left:
                backtrack_dfs(node.left, currArr, currSum)
                print "222", currArr
                currArr.pop()
            if node.right:
                backtrack_dfs(node.right, currArr, currSum)
                print "333", currArr
                currArr.pop()
            #currSum -= node.val
            #currArr.pop()
        
        if not root:
            return []
        res = []
        backtrack_dfs(root, [], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/111428111/

114 / 114 个通过测试用例
状态：通过
执行用时: 668 ms
内存消耗: 15 MB

执行用时：668 ms, 在所有 Python 提交中击败了7.04%的用户
内存消耗：15 MB, 在所有 Python 提交中击败了80.24%的用户
"""
