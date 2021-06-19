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

        # 开始时arr就该做个过滤的，这个做题前还想到了，后来忘了。
        def has_duplicate_char(s):
            se = set()
            for ch in s:
                if ch in se:
                    return True
                else:
                    se.add(ch)
            return False
        for i in range(len(arr)-1, -1, -1):
            if has_duplicate_char(arr[i]):
                arr.pop(i)

        length = len(arr)
        dic = {}
        for i in range(length-1):
            for j in range(i+1, length):
                key1, key2 = str(i) + '--' + str(j), str(j) + '--' + str(i)
                # 干他大爷的，没想到最终的错在这里：比如1和14形成的key 114 会被11和4形成的key（同样是114）改掉。。。
                # 所以要么老老实实用tuple，要么多个连接符之类的。
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
                    if dic[str(existingInd) + '--' + str(ind)]:
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
https://leetcode-cn.com/submissions/detail/188014038/

85 / 85 个通过测试用例
状态：通过
执行用时: 212 ms
内存消耗: 13.6 MB

执行用时：212 ms, 在所有 Python 提交中击败了9.68%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了51.61%的用户
"""
