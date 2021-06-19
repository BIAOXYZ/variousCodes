class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """

        # 回溯算法，打算先用个哈希表预存一下任意两个字符串之间是否有公共字符这个关系的结果，
        # has_common_char 这个函数的功能也可以通过引入位运算来搞定。

        def has_common_char(s1, s2):
            for ch in s1:
                if ch in s2:
                    return True
            return False

        length = len(arr)
        dic = {}
        for i in range(length-1):
            for j in range(i+1, length):
                key1, key2 = str(i) + str(j), str(j) + str(i)
                dic[key1] = dic[key2] = has_common_char(arr[i], arr[j])
        
        # 还是python变量作用域的问题，我怀疑用python3的nonlocal能解决。。。
        # maxLen = 0
        maxLen = [0]
        def backtrack(currIndArr, pos):
            ##print currIndArr, pos, "--", maxLen
            if pos == length:
                currLen = 0
                for ind in currIndArr:
                    currLen += len(arr[ind])
                # maxLen = max(maxLen, currLen)
                maxLen[0] = max(maxLen[0], currLen)
                return
            for ind in range(pos, length):
                flag = True
                for existingInd in currIndArr:
                    if dic[str(existingInd) + str(ind)]:
                        flag = False
                        break
                if flag:
                    # 有当前元素 ind 时往下接着探索
                    currIndArr.append(ind)
                    backtrack(currIndArr, ind+1)
                    currIndArr.pop()
                # 没有当前元素 ind 时往下接着探索（但是仔细想想这个分支应该没用？因为前面flag为真时会包含？）
                ## 试试不要这个分支看能不能省点时间——至少上一个超时用例能过了。。。
                ## backtrack(currIndArr, pos+1)
                else:
                    # 实际上不是只有到末尾了才求一下最长长度，任何一个不能往下延续的都可以求。
                    currLen = 0
                    for ind in currIndArr:
                        currLen += len(arr[ind])
                    maxLen[0] = max(maxLen[0], currLen)
        
        backtrack([], 0)
        return maxLen[0]
        
"""
https://leetcode-cn.com/submissions/detail/187984499/

70 / 85 个通过测试用例
状态：解答错误

最后执行的输入：
["yy","bkhwmpbiisbldzknpm"]
输出：
20
预期结果：
0
"""
