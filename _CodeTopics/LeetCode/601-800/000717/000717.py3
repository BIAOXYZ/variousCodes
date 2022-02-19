class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        # 对于每次的第一个 1 来说，必须要和紧挨着的下一个元素结合，
        # 才能合法。而对于那些 0 直接过就可以。

        length = len(bits)
        # 其实 stk 用个 flag 就可以。
        stk = []
        for i in range(length-1):
            if not stk:
                if bits[i] == 1:
                    stk.append(1)
                else:
                    continue
            else:
                stk.pop()
        return True if not stk else False
        
"""
https://leetcode-cn.com/submissions/detail/270542210/

执行用时：32 ms, 在所有 Python3 提交中击败了78.60%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了17.19%的用户
通过测试用例：
93 / 93
"""
