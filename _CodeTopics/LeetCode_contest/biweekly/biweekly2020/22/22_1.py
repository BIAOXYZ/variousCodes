class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        
        """
        res = 0   
        for i in range(len(arr1)):
            flag = 1
            for j in range(len(arr2)):
                if 0 < arr1[i] - arr2[j] <= d or 0 > arr1[i] - arr2[j] >= -d:
                    flag = 0
                    break            
            if flag == 1:
                res+=1
        return res
        """
        
        res = 0   
        for i in range(len(arr1)):
            flag = 0
            for j in range(len(arr2)):
                if arr1[i] - arr2[j] < -d or arr1[i] - arr2[j] > d:
                    flag = 1
                    continue
                else:
                    flag = 0
                    break            
            if flag is 1:
                res+=1
        return res
