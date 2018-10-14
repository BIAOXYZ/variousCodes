import sys

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

class Test():
    def run(self, listofnums, targetvalue):
        sol = Solution()
        res = sol.twoSum(listofnums, targetvalue)
        print ("The indices for the list %s to obtain %s is %s" % (listofnums, targetvalue, res))

if  __name__ == '__main__':
    print("------------------------------\nThe main program will start!\n------------------------------\n")
    print("The default coding is:", sys.getdefaultencoding())
    print("\n")

    nums1 = [1, 4, 34, 9, 10, 123]; target1 = 124
    nums2 = [8, 12, 100]; target2 = 500

    test = Test()
    test.run(nums1, target1)
    test.run(nums2, target2)

    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")
