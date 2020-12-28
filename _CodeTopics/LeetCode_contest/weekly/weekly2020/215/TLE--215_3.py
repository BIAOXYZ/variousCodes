class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
        def backtrack(currNums, currX, steps):
            if currX < 0:
                return
            elif currX == 0:
                res[0] = min(res[0], steps)
                return
            else:
                if not currNums:
                    return
                else:
                    backtrack(currNums[1:], currX-currNums[0], steps+1)
                    if len(currNums) > 1:
                        backtrack(currNums[:len(currNums)-1], currX-currNums[-1], steps+1)
        
        res = [float('inf')]
        backtrack(nums,x,0)
        if res[0] == float('inf'):
            return -1
        return res[0]
    
"""
https://leetcode-cn.com/submissions/detail/123526453/

8 / 86 个通过测试用例
状态：超出时间限制

最后执行的输入：
[1241,8769,9151,3211,2314,8007,3713,5835,2176,8227,5251,9229,904,1899,5513,7878,8663,3804,2685,3501,1204,9742,2578,8849,1120,4687,5902,9929,6769,8171,5150,1343,9619,3973,3273,6427,47,8701,2741,7402,1412,2223,8152,805,6726,9128,2794,7137,6725,4279,7200,5582,9583,7443,6573,7221,1423,4859,2608,3772,7437,2581,975,3893,9172,3,3113,2978,9300,6029,4958,229,4630,653,1421,5512,5392,7287,8643,4495,2640,8047,7268,3878,6010,8070,7560,8931,76,6502,5952,4871,5986,4935,3015,8263,7497,8153,384,1136]
894887480
"""
