class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        # 第 257 场周赛第二题
        # https://leetcode-cn.com/submissions/detail/215334740/
        # PS：相比原版有小的改动，主要是构建 dic2 的部分 —— 我认为原版虽然过了，
        #     但是其实是有问题的，因为在 i = 0 时也用到了 keys[i-1]，那不就跑
        #     到最后一个元素了？所以当时的程序能过应该只是用例没测出来。。。

        n = len(properties)
        dic = {}
        for p in properties:
            if p[0] in dic:
                dic[p[0]] = max(dic[p[0]], p[1])
            else:
                dic[p[0]] = p[1]
        
        keys = list(dic.keys())
        keys.sort(reverse=True)
        m = len(keys)
        dic2 = {keys[0] : dic[keys[0]]}
        for i in range(1, m):
            currKey, prevKey = keys[i], keys[i-1]
            dic2[currKey] = max(dic[prevKey], dic2[prevKey])
        
        maxKey = max(keys)
        properties.sort()
        res = 0
        for i in range(n-1):
            p = properties[i]
            if p[0] == maxKey:
                return res
            if p[1] < dic2[p[0]]:
                res += 1
        return res
        
"""
https://leetcode-cn.com/submissions/detail/263040972/

执行用时：672 ms, 在所有 Python3 提交中击败了19.05%的用户
内存消耗：61.4 MB, 在所有 Python3 提交中击败了5.44%的用户
通过测试用例：
44 / 44
"""
