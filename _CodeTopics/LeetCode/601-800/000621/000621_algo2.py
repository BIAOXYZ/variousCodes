class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        # 类似官方答案 方法二：构造 的思想，同时参考了如下实现：
        # https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/

        dic = {}
        for ch in tasks:
            if dic.has_key(ch):
                dic[ch] += 1
            else:
                dic[ch] = 1
        keyList = dic.keys()
        keyList.sort(key=lambda k:dic[k], reverse=True)
        maxFreq = dic[keyList[0]]

        res = (maxFreq - 1) * (n + 1)
        for freq in sorted(dic.values(), reverse=True):
            if freq == maxFreq:
                res += 1
            else:
                break
        
        return res if res > len(tasks) else len(tasks)
        
"""
https://leetcode-cn.com/submissions/detail/128871614/

71 / 71 个通过测试用例
状态：通过
执行用时: 108 ms
内存消耗: 14.5 MB

执行用时：108 ms, 在所有 Python 提交中击败了63.28%的用户
内存消耗：14.5 MB, 在所有 Python 提交中击败了12.86%的用户
"""
