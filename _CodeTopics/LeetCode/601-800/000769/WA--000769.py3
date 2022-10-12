class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        def find_max_and_count_the_left_part(lis):
            maxElem = max(lis)
            ind = lis.index(maxElem)
            if ind == 0:
                return 1
            else:
                return 1 + find_max_and_count_the_left_part(lis[:ind])
        return find_max_and_count_the_left_part(arr)
        
"""
https://leetcode.cn/submissions/detail/372474258/

30 / 52 个通过测试用例
状态：解答错误

输入：
[1,2,0,3]
输出：
3
预期结果：
2
"""
