class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        length = len(preorder)
        # direction通过长度和值，来表示当前应该去搜索第 len(direction) 层的左/右子树了。
        # 比如初始时 ['l'] 表示当前应该去遍历第一层（也就是根结点）的左子树了。
        direction = ['l']

        for i in range(1, length):
            ch = preorder[i]
            if ch == ",":
                continue
            if ch.isdigit():
                direction.append("l")
            elif ch == "#":
                if direction[-1] == "l":
                    direction[-1] = "r"
                else:
                    while direction and direction[-1] == "r":
                        direction.pop()
                    if direction:
                        direction[-1] = "r"
            ##print "ch is:", ch
            ##print direction
            if (not direction and i < length - 1) or (direction and i == length - 1):
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/154098330/

140 / 150 个通过测试用例
状态：解答错误

输入：
"1"
输出：
true
预期：
false
"""
