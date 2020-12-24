class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        length = len(ratings)
        if length == 0: return 0
        elif length == 1: return 1

        # 主要思想就是把特殊点分成5大类：波峰、波谷、一边平一边是波峰、一边平一边是波谷、两边平。
        # 那么最终就是从每个波谷和单边波谷出发，不断向两边加1加2加3...等等。直到碰到波峰、单边波峰
        # 单边波谷、两边平，就会停下来。有两个细节需要处理：
        # 1.波峰涉及到从两边递增过来，所以需要用较大的那个。
        # 2.两面平的点有可能因为取较大值的操作给更新成非1，其实两面平的点就是取1就对了。
        dic = {'crest':[], 'trough':[], 'flat_crest':[], 'flat_trough':[], 'flat':[]}

        if ratings[0] > ratings[1]:
            dic['crest'].append(0)
        elif ratings[0] < ratings[1]:
            dic['trough'].append(0)
        else:
            dic['flat'].append(0)
        
        if ratings[-1] > ratings[-2]:
            dic['crest'].append(length-1)
        elif ratings[-1] < ratings[-2]:
            dic['trough'].append(length-1)
        else:
            dic['flat'].append(length-1)
        
        for i in range(1, length-1):
            if (ratings[i] - ratings[i-1]) * (ratings[i] - ratings[i+1]) > 0:
                if ratings[i] - ratings[i-1] > 0:
                    dic['crest'].append(i)
                else:
                    dic['trough'].append(i)
            elif (ratings[i] - ratings[i-1]) * (ratings[i] - ratings[i+1]) == 0:
                if ratings[i] == ratings[i-1] == ratings[i+1]:
                    dic['flat'].append(i)
                else:
                    if 2*ratings[i] - ratings[i-1] - ratings[i+1] > 0:
                        dic['flat_crest'].append(i)
                    else:
                        dic['flat_trough'].append(i)
        
        endPos =  dic['crest'] + dic['flat_crest'] + dic['flat_trough'] + dic['flat']
        lis = [1 for _ in range(length)]
        for ind in dic['trough'] + dic['flat_trough']:
            i = 1
            while ind + i <= length - 1 and ind + i not in endPos:
                lis[ind+i] = 1 + i
                i += 1
            if ind + i <= length - 1:
                lis[ind+i] = max(lis[ind+i], 1+i)
            j = 1
            while ind - j >= 0 and ind - j not in endPos:
                lis[ind-j] = 1 + j
                j += 1
            if ind - j >= 0:
                lis[ind-j] = max(lis[ind-j], 1+j)
        # 前面一轮循环完成后有可能把两面平的点更新成非1的值，其实两面平的点只要1就行。
        # 比如如果没有下面这个for循环，输入为[1,2,2,2,3,2,6,5,6,8,10,11,11]时，
        # 打印的错误lis为：[1, 2, 2, 1, 2, 1, 2, 1, 2, 3, 4, 5, 1]，且错误结果为27。
        # 正确的lis应该为：[1, 2, 1, 1, 2, 1, 2, 1, 2, 3, 4, 5, 1]，且正确结果为26。
        for ind in dic['flat']:
            lis[ind] = 1
        print lis
        return sum(lis)
        
"""
https://leetcode-cn.com/submissions/detail/133376229/

43 / 48 个通过测试用例
状态：解答错误

输入：
[1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4]
输出：
49
预期：
47
"""
