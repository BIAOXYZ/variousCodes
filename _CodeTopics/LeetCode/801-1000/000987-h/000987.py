# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        dic = {(0,0) : [root.val]}
        def dfs(node, row, col):
            if node.left:
                coordinate = (row+1, col-1)
                if coordinate in dic:
                    dic[coordinate].append(node.left.val)
                else:
                    dic[coordinate] = [node.left.val]
                dfs(node.left, row+1, col-1)
            if node.right:
                coordinate = (row+1, col+1)
                if coordinate in dic:
                    dic[coordinate].append(node.right.val)
                else:
                    dic[coordinate] = [node.right.val]
                dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        ##print dic
        coors = dic.keys()
        coors.sort(key = lambda x : (x[1], x[0]))
        ##print coors

        maxCol = 1000
        res = []
        currNodeList, currCol = [], maxCol + 1
        for coor in coors:
            if coor[1] != currCol:
                res.append(currNodeList[:])
                currCol = coor[1]
                currNodeList = []
            currNodeList.extend(sorted(dic[coor]))
        res.append(currNodeList[:])
        res.pop(0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/201792260/

32 / 32 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 13.6 MB

执行用时：24 ms, 在所有 Python 提交中击败了47.06%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了17.65%的用户
"""
