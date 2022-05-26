class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:

        # 用哈希表记录每个单词所有的 index；当需要查询两个单词的距离时，对两个索引集合做归并。

        indexDic = defaultdict(list)
        for i, word in enumerate(words):
            indexDic[word].append(i)

        def merge_and_calculate_min_distance(w1, w2):
            l1, l2 = indexDic[w1], indexDic[w2]
            l = []
            ind1 = ind2 = 0
            currMin = float('inf')
            while ind1 < len(l1) or ind2 < len(l2):
                # 此时需要merge进 l 的元素应该是 l1 当前的元素
                if ind1 < len(l1) and (ind2 == len(l2) or l1[ind1] < l2[ind2]):
                    if l and l[-1][0] == 'w2':
                        currMin = min(currMin, l1[ind1] - l2[ind2 - 1])
                    l.append(['w1', l1[ind1]])
                    ind1 += 1
                # 此时需要merge进 l 的元素应该是 l2 当前的元素
                elif ind2 < len(l2) and (ind1 == len(l1) or l2[ind2] < l1[ind1]):
                    if l and l[-1][0] == 'w1':
                        currMin = min(currMin, l2[ind2] - l1[ind1 - 1])
                    l.append(['w2', l2[ind2]])
                    ind2 += 1
            return currMin
        
        return merge_and_calculate_min_distance(word1, word2) if word1 != word2 else 0
        
"""
https://leetcode.cn/submissions/detail/318534894/

执行用时：
124 ms
, 在所有 Python3 提交中击败了
46.06%
的用户
内存消耗：
31.2 MB
, 在所有 Python3 提交中击败了
9.45%
的用户
通过测试用例：
43 / 43
"""
