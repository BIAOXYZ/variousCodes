class Solution(object):
    def checkOverlap(self, radius, x_center, y_center, x1, y1, x2, y2):
        """
        :type radius: int
        :type x_center: int
        :type y_center: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        
        if x_center + radius < x1 or x_center - radius > x2 or y_center + radius < y1 or y_center - radius > y2:
            return False
        else:
            return True

"""
85 / 86 个通过测试用例
输入： 1415
      807
      -784
      -733
      623
      -533
      1005
输出： true
预期： false
"""
"""
第一题系统坑了我好久（第一次错误后改对了，但是在页面上试输入9999，返回结果一直是1，最后提交明明过了），
再加上今天状态不咋地，这个题else直接return True还是漏考虑情况了。
"""
