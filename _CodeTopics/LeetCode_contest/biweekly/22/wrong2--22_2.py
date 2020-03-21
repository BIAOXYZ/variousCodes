class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        
        # 合法的四人家庭座位只能是2345，4567，6789，也就是left4，mid4，right4
        # 每一排的1号和10号座位对能否安排四人家庭无任何影响
        # 23和89是对称的，若被占了，分别会影响left4和right4
        # 45和67是对称的，若被占了，分别会影响 left4+mid4 和 right4+mid4
        
        dic = {}
        for i in range(1, n+1):
            dic[i]=[1,1,1]
        
        for reservedseat in reservedSeats:
            if reservedseat[1] == 1 or reservedseat[1] == 10:
                continue
            if reservedseat[1] == 2 or reservedseat[1] == 3:
                dic[reservedseat[0]][0] = 0
            if reservedseat[1] == 8 or reservedseat[1] == 9:
                dic[reservedseat[0]][2] = 0
            if reservedseat[1] == 4 or reservedseat[1] == 5:
                dic[reservedseat[0]][0] = 0
                dic[reservedseat[0]][1] = 0
            if reservedseat[1] == 6 or reservedseat[1] == 7:
                dic[reservedseat[0]][1] = 0
                dic[reservedseat[0]][2] = 0
        
        max4family = 0
        for row in range(1, n+1):
            sum = dic[row][0] + dic[row][1] + dic[row][2]
            """
            # 这里下面这个if的顺序就有问题了。本来[left,mid,right]为[1,1,1]型的应该
            # 能容纳两个4人家庭的，要是这么写也会变成只能容纳一个！
            if sum == 3:
                sum = 2
            if sum == 2:
                sum = 1
            """
            if sum == 2:
                sum = 1
            if sum == 3:
                sum = 2
            max4family+=sum
        return max4family

"""
# 这次感觉代码应该是没问题，但是内存超了，回头优化吧。

提交结果：执行出错 
执行错误信息：Line 15: MemoryError
最后执行的输入：1000000000
[[819881,3],[796572,1],[498217,4],[219145,3],[12808,5],[478188,4],[563665,5],[461492,4],[49556,4],[192541,4],[11569
"""
