class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dic = {}
        for i, num in enumerate(nums):
            if num in dic:
                # 其实 dic[num] 不需要搞成 list，只要永远记住最新的下标即可。
                # 但是也无所谓了，反正要翻译成C++，就当添加点难度了。。。
                if i - dic[num][-1] <= k:
                    return True
                else:
                    dic[num].append(i)
            else:
                dic[num] = [i]
        return False
        
"""
https://leetcode-cn.com/submissions/detail/260011320/

执行用时：88 ms, 在所有 Python3 提交中击败了51.37%的用户
内存消耗：32 MB, 在所有 Python3 提交中击败了10.99%的用户
通过测试用例：
51 / 51
"""
