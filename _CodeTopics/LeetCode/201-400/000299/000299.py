class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        def str_and_index_to_dict(s):
            dic = {}
            for i, ch in enumerate(s):
                dic[i] = ch
            return dic
        
        def list_intersection(l1, l2):
            res = []
            for elem in l1:
                if elem in l2:
                    res.append(elem)
                    l2.remove(elem)
            return res

        dicS = str_and_index_to_dict(secret)
        dicG = str_and_index_to_dict(guess)
        same = diff = 0
        for k, v in dicS.items():
            if v == dicG[k]:
                same += 1
                del dicS[k]
                del dicG[k]
        
        valS, valG = dicS.values(), dicG.values()
        diff = len(list_intersection(valS, valG))
        return str(same) + 'A' + str(diff) + 'B'
        
"""
https://leetcode-cn.com/submissions/detail/236484334/

执行用时：64 ms, 在所有 Python 提交中击败了21.62%的用户
内存消耗：13.5 MB, 在所有 Python 提交中击败了8.11%的用户
通过测试用例：
152 / 152
"""
