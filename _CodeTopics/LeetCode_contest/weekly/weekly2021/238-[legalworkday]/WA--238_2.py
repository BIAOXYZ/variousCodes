class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        ctr = collections.Counter(nums)
        newnum = list(set(nums))
        newnum.sort()
        
        n = len(newnum)
        incr = [0] * n
        for i in range(1, n):
            tmp = 0
            tmpk = k
            for j in range(i-1, -1, -1):
                if tmpk >= ctr[newnum[j]] * (newnum[i] - newnum[j]):
                    tmp += ctr[newnum[j]]
                    tmpk -= ctr[newnum[j]] * (newnum[i] - newnum[j])
                    continue
                else:
                    while tmpk > newnum[i] - newnum[j]:
                        tmp += 1
                        tmpk -= newnum[i] - newnum[j]
            incr[i] = tmp + ctr[newnum[i]]
        return max(incr)
    
"""
https://leetcode-cn.com/submissions/detail/171670976/

60 / 65 个通过测试用例
状态：解答错误

最后执行的输入：
[9979,9938,9947,9916,9995,9981,9981,9931,9984,9942,9946,9946,9945,9931,9908,9920,9929,9917,9904,9945,9963,9910,9942,9965,9915,9981,9908,9919,9975,9904,9934,9922,9989,9946,9928,9928,9940,9941,9995,9905,9903,9980,9917,9940,9910,9994,9909,9965,9972,9931,9975,9913,9983,9943,9996,9917,9994,9991,9948,9961,9921,9981,9928,9933,9905,9957,9953,9940,9958,9982,9900,9912,9959,9992,9978,9988,9940,9985,9945,9900,9956,9976,9972,9914,9903,9978,9965,9987,9926,9963,9968,9962,9995,9963,9960,9986,9916,9911,9976,9988,9952,9914,9934,9929,9962,9999,9988,9901,9925,9983,9991,9915,9930,9949,9931,9944,9947,9921,9982,9984,9998,9945,9907,9900,9992,9945,9995,9941,9930,9918,9961,9960,9900,9952,9952,9954,9976,9970,9990,9947,9910,9908,9935,9971,9971,10000,9941,9983,9949,9985,9992,9996,9918,9930,9994,9970,9989,9975,9960,9973,9993,9900,9915,9974,9966,9978,9926,9937,9936,9952,9996,9996,9912,9915,9976,9976,9901,9926,9959,9989,9976,9904,9999,9925,9934,9947,9950,9985,9985,9932,9922,9962,9962,9993,9912,9924,9992,9941,9959,9954,9943,9995,9992,9928,9992,9920,9984,9917,9976,9971,9927,9917,9923,9948,9929,9990,9990,9921,9989,9910,9921]
2636
"""
