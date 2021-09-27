# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        # 这道题还挺新颖的感觉。想法是用一个列表表示当前状态，其含义是以该点为末尾的所有可能路径和。
        # 构造方法就是：每次新往下走一层，前面的元素都加上新元素的值，然后数组末尾还要append一下新元素的值。
        ## 每次往上一层走，数组除了最后一个元素，前面每一个都减去最后一个元素，然后最后一个元素还要pop出去。
        # 比如对于输入 [10,5,-3,3,2,null,11,3,-2,null,1]，在root时，这个状态数组是 [10]，
        ## 紧接着到了一下层左边，就会变成 [15, 5]，再左下一次，变成 [18, 8, 3]，依次类推。
        ## 返回的时候就反过来： [18, 8, 3] -- [18-3, 8-3, 3(pop掉)] = [15, 5]，依次类推。

        res = [0]
        def dfs_with_state(node, arr):
            for i in range(len(arr)):
                arr[i] += node.val
                if arr[i] == targetSum:
                    res[0] += 1
            arr.append(node.val)
            if node.val == targetSum:
                res[0] += 1
            if node.left:
                dfs_with_state(node.left, arr)
            if node.right:
                dfs_with_state(node.right, arr)
            for i in range(len(arr) - 1):
                arr[i] -= node.val
            arr.pop()
        
        dfs_with_state(root, [])
        return res[0]
        
"""
https://leetcode-cn.com/submissions/detail/223930169/

2 / 126 个通过测试用例
状态：执行出错

执行出错信息：
AttributeError: 'NoneType' object has no attribute 'val'
    arr.append(node.val)
Line 28 in dfs_with_state (Solution.py)
    dfs_with_state(root, [])
Line 39 in pathSum (Solution.py)
    ret = Solution().pathSum(param_1, param_2)
Line 67 in _driver (Solution.py)
    _driver()
Line 77 in <module> (Solution.py)
最后执行的输入：
[]
1
"""
