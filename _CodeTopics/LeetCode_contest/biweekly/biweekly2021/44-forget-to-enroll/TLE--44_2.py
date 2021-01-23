class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """

        def has_intersection(l1, l2):
            for elem in l1:
                if elem in l2:
                    return True
            return False
        
        languages = ["placeholder"] + languages
        needteach = [float('inf')] + [0] * n
        for i in range(1, n+1):
            lang = copy.deepcopy(languages)
            print lang
            for friend in friendships:
                l1 = lang[friend[0]]
                l2 = lang[friend[1]]
                if not has_intersection(l1, l2):
                    if i not in lang[friend[0]]:
                        lang[friend[0]].append(i)
                        needteach[i] += 1
                    if i not in lang[friend[1]]:
                        lang[friend[1]].append(i)
                        needteach[i] += 1
        print needteach
        return min(needteach)
    
"""
https://leetcode-cn.com/submissions/detail/140644995/

58 / 99 个通过测试用例
状态：超出时间限制
"""
