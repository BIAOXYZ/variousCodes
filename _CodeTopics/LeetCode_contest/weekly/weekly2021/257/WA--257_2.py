class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        
        n = len(properties)
        properties.sort()
        res = 0
        for i in range(n-1):
            small, large = properties[i], properties[i+1]
            if small[1] < large[1]:
                res += 1
        return res
    
"""
https://leetcode-cn.com/submissions/detail/215309817/

11 / 44 个通过测试用例
状态：解答错误

最后执行的输入：
[[1,1],[2,1],[2,2],[1,2]]
输入：
[[1,1],[2,1],[2,2],[1,2]]
输出：
2
预期：
1
"""
