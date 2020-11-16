class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people.sort(key = lambda x:(x[1],x[0]))
        #print people
        """
        输入：
        [[4,0],[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

        经过上面的排序后：
        [[4, 0], [5, 0], [7, 0], [6, 1], [7, 1], [5, 2], [4, 4]]
        """

        res = []
        for person in people:
            if person[1] == 0:
                res.append(person)
            else:
                count = 0
                for i, elem in enumerate(res):
                    if elem[0] >= person[0]:
                        count += 1
                        if count == person[1]:
                            i += 1
                            while i <= len(res)-1 and person[0] > res[i][0]:
                                i += 1
                            res.insert(i, person)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/123764901/

37 / 37 个通过测试用例
状态：通过
执行用时: 492 ms
内存消耗: 13.4 MB

执行用时：492 ms, 在所有 Python 提交中击败了6.56%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了26.67%的用户
"""
