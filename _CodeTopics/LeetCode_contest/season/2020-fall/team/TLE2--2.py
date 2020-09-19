class Solution(object):
    def isMagic(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        
        def reorder(arr):
            res = []
            for i in range(1,len(arr)):
                if (i + 1) % 2 == 0:
                    res.append(arr[i])
                    arr[i] = "delete"
            while "delete" in arr:
                arr.remove("delete")
            return res + arr
        
        def backtrack(currArr, k, pos):
            afterReorder = reorder(currArr)
            if len(afterReorder) <= k:
                if afterReorder == target[pos:]:
                    return True
                return False
            arr1, arr2 = afterReorder[:k], afterReorder[k:]
            if arr1 == target[pos:pos+k]:
                return backtrack(arr2, k, pos+k)
            else:
                return False
            
        n = len(target)
        arr = range(1,n+1)
        for k in range(1,n+1):
            if backtrack(arr[:], k, 0):
                return True
        return False
    
"""
https://leetcode-cn.com/contest/season/2020-fall/submissions/109544608/
"""
