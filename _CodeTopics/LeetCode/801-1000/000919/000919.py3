# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.lis = [[root]]
        stk = [root]
        while stk:
            nextLevel = []
            for node in stk:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            stk = nextLevel
            if nextLevel:
                self.lis.append(nextLevel[:])

    def insert(self, val: int) -> int:
        newNode = TreeNode(val)
        level, nextPos = len(self.lis)-1, len(self.lis[-1])
        if nextPos == 2**level:
            father = self.lis[-1][0]
            father.left = newNode
            self.lis.append([newNode])
        else:
            fatherInd = nextPos // 2
            father = self.lis[-2][fatherInd]
            if nextPos & 1 == 1:
                father.right = newNode
            else:
                father.left = newNode
            self.lis[-1].append(newNode)
        return father.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

"""
https://leetcode.cn/submissions/detail/341247513/

执行用时：
60 ms
, 在所有 Python3 提交中击败了
39.11%
的用户
内存消耗：
16.1 MB
, 在所有 Python3 提交中击败了
35.75%
的用户
通过测试用例：
84 / 84
"""
