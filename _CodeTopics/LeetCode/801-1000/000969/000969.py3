class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        # 开始没有思路，后来想从dp下手，但是感觉状态好像有点多。
        # 接着想到归纳法：
        # - 长度为 1 的数组 [1] 不用说了；
        # - 长度为 2 的数组只能是 [1,2] 或 [2,1]，也很明显；
        # - 假设长度为 n-1 数组（不管任何局面开头）都有排法，那么对于
        #   长度为 n 的数组，只要先把 n 排到最后一位，然后调用 n-1 长度的排法即可。
        #   把 n 排到最后一位仅需两步：不管 n 在哪，先煎饼排序一次把它排到最靠前的位置；
        #   然后“全量”煎饼排序一次，就可以把 n 放到末尾了。

        def reverse_slice(lis, left, right):
            if left > right:
                raise Exception("The interval is not correct")
            while left < right:
                lis[left], lis[right] = lis[right], lis[left]
                left += 1
                right -= 1
        
        res = []
        def pancake_sort_fixed_length(lis, length):
            if length == 1:
                return
            if lis[-1] == length:
                pancake_sort_fixed_length(lis[:-1], length-1)
            # 最大的那个元素在第一个位置，此时只需要一次全量reverse即可。
            elif lis[0] == length:
                res.append(length)
                lis.reverse()
                pancake_sort_fixed_length(lis[:-1], length-1)        
            else:
                ind = lis.index(length)
                res.append(ind+1)
                res.append(length)
                reverse_slice(lis, 0, ind)
                lis.reverse()
                pancake_sort_fixed_length(lis[:-1], length-1)
        
        pancake_sort_fixed_length(arr, len(arr))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/270139423/

执行用时：40 ms, 在所有 Python3 提交中击败了52.83%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.96%的用户
通过测试用例：
215 / 215
"""
