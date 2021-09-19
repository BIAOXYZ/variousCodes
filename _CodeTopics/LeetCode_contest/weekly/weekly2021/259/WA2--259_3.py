class DetectSquares(object):

    def __init__(self):
        
        self.dic = {}
        self.dicx = {}
        self.dicy = {}

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        
        k = tuple(point)
        x, y = point[0], point[1]
        self.dic[k] = self.dic.setdefault(k, 0) + 1
        if x in self.dicx:
            self.dicx[x].add(k)
        else:
            self.dicx[x] = set([k])
        if y in self.dicy:
            self.dicy[y].add(k)
        else:
            self.dicy[y] = set([k])
        print self.dic
        print self.dicx
        print self.dicy
        print "\n"

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        
        x, y = point[0], point[1]
        res = 0
        
        xset = self.dicx.get(x, None)
        yset = self.dicy.get(y, None)
        if not xset or not yset:
            return 0
        
        for samex in xset:
            if samex == point:
                continue
            newy = samex[1]
            for samey in yset:
                if samex == point:
                    continue
                newx = samey[0]
                key = (newx, newy)
                if key in self.dic:
                    res += self.dic[samex] * self.dic[samey] * self.dic[key]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

"""
https://leetcode-cn.com/submissions/detail/220996973/

16 / 51 个通过测试用例
状态：解答错误

输入：
["DetectSquares","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count"]
[[],[[5,10]],[[10,5]],[[10,10]],[[5,5]],[[3,0]],[[8,0]],[[8,5]],[[3,5]],[[9,0]],[[9,8]],[[1,8]],[[1,0]],[[0,0]],[[8,0]],[[8,8]],[[0,8]],[[1,9]],[[2,9]],[[2,10]],[[1,10]],[[7,8]],[[2,3]],[[2,8]],[[7,3]],[[9,10]],[[9,5]],[[4,5]],[[4,10]],[[0,9]],[[4,5]],[[4,9]],[[0,5]],[[1,10]],[[10,1]],[[10,10]],[[1,1]],[[10,0]],[[2,0]],[[2,8]],[[10,8]],[[7,6]],[[4,6]],[[4,9]],[[7,9]],[[10,9]],[[10,0]],[[1,0]],[[1,9]],[[0,9]],[[8,1]],[[0,1]],[[8,9]],[[3,9]],[[10,9]],[[3,2]],[[10,2]],[[3,8]],[[9,2]],[[3,2]],[[9,8]],[[0,9]],[[7,9]],[[0,2]],[[7,2]],[[10,1]],[[1,10]],[[10,10]],[[1,1]],[[6,10]],[[2,6]],[[6,6]],[[2,10]],[[6,0]],[[6,2]],[[8,2]],[[8,0]],[[6,5]],[[7,4]],[[6,4]],[[7,5]],[[2,10]],[[8,4]],[[2,4]],[[8,10]],[[2,6]],[[2,5]],[[1,5]],[[1,6]],[[10,9]],[[10,0]],[[1,9]],[[1,0]],[[0,9]],[[5,9]],[[0,4]],[[5,4]],[[3,6]],[[9,0]],[[3,0]],[[9,6]],[[0,2]],[[1,1]],[[0,1]],[[1,2]],[[1,7]],[[8,0]],[[8,7]],[[1,0]],[[2,7]],[[4,5]],[[2,5]],[[4,7]],[[6,7]],[[3,7]],[[6,4]],[[3,4]],[[10,2]],[[2,10]],[[2,2]],[[10,10]],[[10,1]],[[1,10]],[[1,1]],[[10,10]],[[2,10]],[[2,9]],[[3,9]],[[3,10]],[[10,1]],[[1,10]],[[1,1]],[[10,10]],[[10,4]],[[10,3]],[[9,4]],[[9,3]],[[6,6]],[[6,10]],[[10,6]],[[10,10]],[[9,7]],[[4,7]],[[9,2]],[[4,2]],[[2,3]],[[2,1]],[[0,3]],[[0,1]],[[2,8]],[[10,8]],[[2,0]],[[10,0]],[[8,4]],[[2,10]],[[8,10]],[[2,4]],[[0,0]],[[9,9]],[[0,9]],[[9,0]],[[5,7]],[[5,8]],[[4,7]],[[4,8]],[[10,10]],[[10,1]],[[1,1]],[[1,10]],[[6,8]],[[7,8]],[[6,9]],[[7,9]],[[4,6]],[[1,6]],[[4,3]],[[1,3]],[[10,1]],[[1,10]],[[10,10]],[[1,1]],[[7,7]],[[7,10]],[[4,7]],[[4,10]],[[0,0]],[[8,0]],[[0,8]],[[8,8]],[[3,5]],[[2,4]],[[3,4]],[[2,5]],[[0,6]],[[0,2]],[[4,2]],[[4,6]],[[5,2]],[[9,6]],[[9,2]],[[5,6]],[[1,1]],[[1,10]],[[10,10]],[[10,1]],[[7,5]],[[2,0]],[[2,5]],[[7,0]],[[1,9]],[[1,2]],[[8,2]],[[8,9]],[[3,8]],[[3,3]],[[8,3]],[[8,8]],[[3,10]],[[9,10]],[[3,4]],[[9,4]],[[0,2]],[[0,10]],[[8,10]],[[8,2]],[[9,4]],[[8,4]],[[8,5]],[[9,5]],[[9,8]],[[4,3]],[[4,8]],[[9,3]],[[4,9]],[[0,5]],[[0,9]],[[4,5]],[[1,3]],[[3,5]],[[1,5]],[[3,3]],[[0,0]],[[0,8]],[[8,0]],[[8,8]],[[2,8]],[[10,0]],[[10,8]],[[2,0]],[[8,1]],[[0,9]],[[8,9]],[[0,1]],[[4,9]],[[4,6]],[[1,9]],[[1,6]],[[0,9]],[[0,8]],[[1,9]],[[1,8]],[[5,1]],[[5,6]],[[10,1]],[[10,6]],[[9,2]],[[2,2]],[[2,9]],[[9,9]],[[5,5]],[[8,5]],[[5,8]],[[8,8]],[[8,0]],[[1,0]],[[8,7]],[[1,7]],[[8,2]],[[5,5]],[[5,2]],[[8,5]],[[6,6]],[[6,8]],[[8,6]],[[8,8]],[[2,10]],[[10,2]],[[2,2]],[[10,10]],[[1,9]],[[8,2]],[[1,2]],[[8,9]],[[7,4]],[[7,2]],[[9,4]],[[9,2]],[[1,9]],[[1,0]],[[10,0]],[[10,9]],[[2,10]],[[2,3]],[[9,10]],[[9,3]],[[10,0]],[[1,0]],[[1,9]],[[10,9]],[[8,10]],[[1,10]],[[1,3]],[[8,3]],[[0,9]],[[9,9]],[[0,0]],[[9,0]],[[7,9]],[[8,9]],[[7,8]],[[8,8]],[[3,1]],[[9,7]],[[9,1]],[[3,7]],[[5,9]],[[6,9]],[[5,8]],[[6,8]],[[0,1]],[[0,10]],[[9,10]],[[9,1]],[[8,0]],[[8,2]],[[10,2]],[[10,0]],[[8,0]],[[0,8]],[[8,8]],[[0,0]],[[6,7]],[[5,8]],[[5,7]],[[6,8]],[[0,9]],[[0,2]],[[7,9]],[[7,2]],[[5,0]],[[5,5]],[[10,0]],[[10,5]],[[1,10]],[[10,10]],[[10,1]],[[1,1]],[[9,2]],[[9,10]],[[1,2]],[[1,10]],[[1,10]],[[10,1]],[[10,10]],[[1,1]],[[9,9]],[[0,9]],[[0,0]],[[9,0]],[[9,6]],[[9,3]],[[6,3]],[[6,6]],[[10,4]],[[6,0]],[[10,0]],[[6,4]],[[6,8]],[[0,2]],[[0,8]],[[6,2]],[[7,9]],[[0,9]],[[7,2]],[[0,2]],[[9,1]],[[9,10]],[[0,10]],[[0,1]],[[10,0]],[[10,9]],[[1,9]],[[1,0]],[[1,6]],[[1,9]],[[4,9]],[[4,6]],[[0,8]],[[1,9]],[[0,9]],[[1,8]],[[1,1]],[[9,1]],[[1,9]],[[9,9]],[[2,5]],[[2,9]],[[6,5]],[[6,9]],[[7,3]],[[2,3]],[[2,8]],[[7,8]],[[9,4]],[[4,4]],[[9,9]],[[4,9]],[[4,4]],[[2,4]],[[4,2]],[[2,2]],[[0,3]],[[0,2]],[[1,3]],[[1,2]],[[10,9]],[[10,2]],[[3,2]],[[3,9]],[[5,6]],[[10,6]],[[10,1]],[[5,1]],[[9,0]],[[0,9]],[[9,9]],[[0,0]],[[5,6]],[[9,2]],[[9,6]],[[5,2]],[[3,3]],[[10,3]],[[10,10]],[[3,10]],[[2,4]],[[2,10]],[[8,4]],[[8,10]],[[4,9]],[[1,9]],[[4,6]],[[1,6]],[[1,8]],[[9,0]],[[1,0]],[[9,8]],[[10,3]],[[5,8]],[[5,3]],[[10,8]],[[8,2]],[[0,10]],[[8,10]],[[0,2]],[[9,0]],[[2,7]],[[9,7]],[[2,0]],[[0,4]],[[5,9]],[[0,9]],[[5,4]],[[5,3]],[[10,3]],[[5,8]],[[10,8]],[[6,4]],[[7,4]],[[6,5]],[[7,5]],[[9,1]],[[0,1]],[[9,10]],[[0,10]],[[5,10]],[[5,7]],[[8,7]],[[8,10]],[[8,0]],[[8,7]],[[1,7]],[[1,0]],[[1,1]],[[9,9]],[[1,9]],[[9,1]],[[3,1]],[[3,5]],[[7,5]],[[7,1]],[[5,8]],[[5,3]],[[10,8]],[[10,3]],[[0,9]],[[2,7]],[[2,9]],[[0,7]],[[9,3]],[[9,7]],[[5,3]],[[5,7]],[[0,0]],[[9,0]],[[9,9]],[[0,9]],[[6,4]],[[4,2]],[[4,4]],[[6,2]],[[1,9]],[[1,5]],[[5,5]],[[5,9]],[[7,7]],[[0,7]],[[0,0]],[[7,0]],[[1,3]],[[1,9]],[[7,3]],[[7,9]],[[0,9]],[[9,9]],[[9,0]],[[0,0]],[[1,8]],[[3,6]],[[3,8]],[[1,6]]]
输出：
[null,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,3,null,null,null,1,null,null,null,1,null,null,null,2,null,null,null,5,null,null,null,2,null,null,null,15,null,null,null,5,null,null,null,20,null,null,null,23,null,null,null,4,null,null,null,25,null,null,null,8,null,null,null,27,null,null,null,49,null,null,null,54,null,null,null,12,null,null,null,47,null,null,null,28,null,null,null,97,null,null,null,9,null,null,null,29,null,null,null,47,null,null,null,135,null,null,null,20,null,null,null,43,null,null,null,214,null,null,null,268,null,null,null,133,null,null,null,392,null,null,null,24,null,null,null,440,null,null,null,69,null,null,null,231,null,null,null,413,null,null,null,229,null,null,null,234,null,null,null,87,null,null,null,583,null,null,null,118,null,null,null,155,null,null,null,664,null,null,null,265,null,null,null,215,null,null,null,372,null,null,null,184,null,null,null,94,null,null,null,1141,null,null,null,216,null,null,null,424,null,null,null,296,null,null,null,265,null,null,null,426,null,null,null,328,null,null,null,218,null,null,null,360,null,null,null,266,null,null,null,524,null,null,null,1215,null,null,null,997,null,null,null,572,null,null,null,1013,null,null,null,661,null,null,null,983,null,null,null,834,null,null,null,510,null,null,null,925,null,null,null,1029,null,null,null,2299,null,null,null,1705,null,null,null,1018,null,null,null,2503,null,null,null,446,null,null,null,2830,null,null,null,759,null,null,null,1568,null,null,null,1392,null,null,null,432,null,null,null,789,null,null,null,1348,null,null,null,3309,null,null,null,3441,null,null,null,965,null,null,null,1007,null,null,null,1693,null,null,null,3167,null,null,null,4873,null,null,null,3727,null,null,null,2934,null,null,null,655,null,null,null,751,null,null,null,1652,null,null,null,4705,null,null,null,4027,null,null,null,5807,null,null,null,837,null,null,null,4043,null,null,null,5369,null,null,null,3141,null,null,null,1595,null,null,null,3415,null,null,null,4017,null,null,null,5993,null,null,null,3337,null,null,null,1616,null,null,null,7775,null,null,null,2223,null,null,null,2776,null,null,null,5444,null,null,null,3528,null,null,null,3975,null,null,null,5148,null,null,null,7951,null,null,null,6348,null,null,null,1572,null,null,null,5496,null,null,null,1319,null,null,null,11036,null,null,null,6913,null,null,null,9784,null,null,null,6319,null,null,null,2199,null,null,null,4715,null,null,null,3958,null,null,null,2083,null,null,null,18769,null,null,null,3116,null,null,null,7477,null,null,null,3399,null,null,null,5905,null,null,null,13828,null,null,null,5145]
预期：
[null,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,2,null,null,null,1,null,null,null,1,null,null,null,1,null,null,null,2,null,null,null,2,null,null,null,2,null,null,null,2,null,null,null,5,null,null,null,6,null,null,null,2,null,null,null,3,null,null,null,3,null,null,null,14,null,null,null,3,null,null,null,1,null,null,null,2,null,null,null,2,null,null,null,4,null,null,null,20,null,null,null,4,null,null,null,5,null,null,null,10,null,null,null,26,null,null,null,8,null,null,null,3,null,null,null,7,null,null,null,21,null,null,null,20,null,null,null,52,null,null,null,6,null,null,null,56,null,null,null,2,null,null,null,5,null,null,null,17,null,null,null,18,null,null,null,13,null,null,null,19,null,null,null,102,null,null,null,9,null,null,null,2,null,null,null,157,null,null,null,23,null,null,null,29,null,null,null,23,null,null,null,15,null,null,null,24,null,null,null,186,null,null,null,12,null,null,null,32,null,null,null,36,null,null,null,10,null,null,null,35,null,null,null,20,null,null,null,43,null,null,null,48,null,null,null,35,null,null,null,73,null,null,null,59,null,null,null,56,null,null,null,72,null,null,null,198,null,null,null,37,null,null,null,145,null,null,null,130,null,null,null,45,null,null,null,68,null,null,null,172,null,null,null,281,null,null,null,147,null,null,null,53,null,null,null,160,null,null,null,105,null,null,null,253,null,null,null,82,null,null,null,103,null,null,null,248,null,null,null,75,null,null,null,86,null,null,null,312,null,null,null,301,null,null,null,273,null,null,null,119,null,null,null,191,null,null,null,61,null,null,null,584,null,null,null,696,null,null,null,802,null,null,null,293,null,null,null,104,null,null,null,114,null,null,null,242,null,null,null,259,null,null,null,300,null,null,null,465,null,null,null,180,null,null,null,1082,null,null,null,697,null,null,null,187,null,null,null,113,null,null,null,201,null,null,null,520,null,null,null,652,null,null,null,197,null,null,null,91,null,null,null,670,null,null,null,159,null,null,null,189,null,null,null,386,null,null,null,403,null,null,null,204,null,null,null,301,null,null,null,378,null,null,null,314,null,null,null,292,null,null,null,352,null,null,null,174,null,null,null,2778,null,null,null,473,null,null,null,869,null,null,null,1568,null,null,null,190,null,null,null,198,null,null,null,342,null,null,null,286,null,null,null,1062,null,null,null,475,null,null,null,354,null,null,null,174,null,null,null,574,null,null,null,1605,null,null,null,547]
"""
