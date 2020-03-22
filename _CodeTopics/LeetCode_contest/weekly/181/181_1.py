class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        
        # 根据条件，length也等于len(index)
        length = len(nums)   
        target = [None for i in range(length)]
        
        for i in range(length):
            ind = index[i]
            if target[ind] is None:
                target[ind] = nums[i]
            else:
                nextnew = target[ind]
                target[ind] = nums[i]
                #while target[ind+1] is not None:
                for i in range(ind+1, length):
                    temp = target[i]
                    target[i] = nextnew
                    nextnew = temp       
        return target
