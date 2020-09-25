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
            #print "111", currArr
            if currSum == sum and is_leaf(node):
                res.append(currArr[:])
                return
            if currSum > sum or (currSum != sum and is_leaf(node)):
                return
            if node.left:
                backtrack_dfs(node.left, currArr, currSum)
                #print "222", currArr
                currArr.pop()
            if node.right:
                backtrack_dfs(node.right, currArr, currSum)
                #print "333", currArr
                currArr.pop()
            #currSum -= node.val
            #currArr.pop()
        
        if not root:
            return []
        res = []
        backtrack_dfs(root, [], 0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/111427594/

82 / 114 个通过测试用例
状态：解答错误

输入：
[-2,null,-3]
-5
输出：
[]
预期：
[[-2,-3]]
"""
