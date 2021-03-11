class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        length = len(preorder)
        if length == 0 or \
            (length == 1 and preorder[0] != "#") or \
            (length > 1 and preorder[0] == "#"):
            return False

        # direction通过长度和值，来表示当前应该去搜索第 len(direction) 层的左/右子树了。
        # 比如初始时 ['l'] 表示当前应该去遍历第一层（也就是根结点）的左子树了。
        direction = ['l']

        for i in range(1, length):
            ch = preorder[i]
            if ch == ",":
                continue
            if ch.isdigit():
                # 这个是处理有多位数字的情况。。。比如 "9,#,92,#,#" 里的 "92"。
                if i < length - 1 and preorder[i+1].isdigit():
                    continue
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
https://leetcode-cn.com/submissions/detail/154099052/

150 / 150 个通过测试用例
状态：通过
执行用时: 28 ms
内存消耗: 13.4 MB

执行用时：28 ms, 在所有 Python 提交中击败了43.86%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了5.26%的用户
"""
