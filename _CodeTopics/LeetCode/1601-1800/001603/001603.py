class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.capability = [big, medium, small]
        self.park = [0, 0, 0]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.park[carType-1] < self.capability[carType-1]:
            self.park[carType-1] += 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

"""
https://leetcode-cn.com/submissions/detail/156965369/

102 / 102 个通过测试用例
状态：通过
执行用时: 496 ms
内存消耗: 13.6 MB

执行用时：496 ms, 在所有 Python 提交中击败了85.85%的用户
内存消耗：13.6 MB, 在所有 Python 提交中击败了9.91%的用户
"""
