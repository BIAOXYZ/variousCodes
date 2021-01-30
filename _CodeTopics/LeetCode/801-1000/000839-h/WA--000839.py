class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        # 呃，看起来就是并查集的题，但是写了写发现没有用到并查集的俩函数。。。那看来估计会超时？

        def is_similar(s1, s2):
            flag = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    flag += 1
                    if flag > 2:
                        return False
            return True
        
        tmp = [[strs[0]]]
        for i in range(1, len(strs)):
            finished = 0
            for lis in tmp:
                if strs[i] in lis:
                    finished = 1
                    break
                for elem in lis:
                    if is_similar(strs[i], elem):
                        lis.append(strs[i])
                        finished = 1
                        break
            if not finished:
                tmp.append([strs[i]])
        return len(tmp)
        
"""
https://leetcode-cn.com/submissions/detail/142441310/

60 / 77 个通过测试用例
状态：解答错误

输入：
["kccomwcgcs","socgcmcwkc","sgckwcmcoc","coswcmcgkc","cowkccmsgc","cosgmccwkc","sgmkwcccoc","coswmccgkc","kowcccmsgc","kgcomwcccs"]
输出：
6
预期：
5
"""
