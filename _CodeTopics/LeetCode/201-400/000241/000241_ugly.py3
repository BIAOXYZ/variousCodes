class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        n = len(expression)
        lis = []
        tmp = ''
        for ch in expression:
            if ch in '+-*':
                lis.append(tmp)
                lis.append(ch)
                tmp = ''
            else:
                tmp += ch
        lis.append(tmp)

        memoDic = defaultdict(list)
        def memorize_search(strList):
            n = len(strList)
            if n == 1:
                return [int(strList[0])]
            s = ''.join(strList)
            if s in memoDic:
                return memoDic[s]
            # if n == 3:
            #     # 这里当然可以不用 eval，那就是按三种符号分类讨论，但是没有必要那么麻烦了。
            #     res = eval(strList)
            #     memoDic[s].append(res)
            #     return memoDic[s]
            for i in range(1, n, 2):
                # tmplist = strList.copy()
                # leftNum = tmplist.pop(i-1)
                # op = tmplist.pop(i-1)
                # rightNum = tmplist.pop(i-1)
                # tmplist.insert(i-1, str(eval(leftNum + op + rightNum)))
                left, op, right = strList[:i], strList[i], strList[i+1:]
                leftRes, rightRes = memorize_search(left), memorize_search(right)
                for leftNum in leftRes:
                    for rightNum in rightRes:
                        memoDic[s].append(eval(str(leftNum) + op + str(rightNum)))
            return memoDic[s]
        
        return memorize_search(lis)
        
"""
https://leetcode.cn/submissions/detail/331650022/

执行用时：
64 ms
, 在所有 Python3 提交中击败了
7.27%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
38.04%
的用户
通过测试用例：
25 / 25
"""
