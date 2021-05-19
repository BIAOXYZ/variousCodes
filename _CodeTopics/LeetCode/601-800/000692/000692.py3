class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        def list_to_dic_v2(lis):
            dic = {}
            for elem in lis:
                dic[elem] = dic.setdefault(elem, 0) + 1
            return dic
        
        """
        # 本想试试用写好的函数，结果发现 python3 只支持 key=，不支持 cmp= （也不是完全不行，但是比较麻烦）
        # tmp.sort(cmp = complex_compare)
        # 不过代码还是留着吧
        def complex_compare(lis1, lis2):
            freq1, key1 = lis1[1], lis1[0]
            freq2, key2 = lis2[1], lis2[0]
            if freq1 < freq2:
                return lis2
            elif freq1 > freq2:
                return lis1
            else:
                return lis1 if key1 < key2 else lis2
        """

        dic = list_to_dic_v2(words)
        tmp = [[k, v] for k, v in dic.items()]
        # 同样的代码放 Python2 里就不行，有unicode的问题，嫌麻烦先用Python3了，后面再看Python2里怎么改。
        ## print(tmp)
        tmp.sort(key = lambda x : (-x[1], x[0]))
        res = [tmp[i][0] for i in range(k)]
        return res
        
"""
https://leetcode-cn.com/submissions/detail/179113321/

110 / 110 个通过测试用例
状态：通过
执行用时: 84 ms
内存消耗: 15.1 MB

执行用时：84 ms, 在所有 Python3 提交中击败了13.00%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了8.58%的用户
"""
