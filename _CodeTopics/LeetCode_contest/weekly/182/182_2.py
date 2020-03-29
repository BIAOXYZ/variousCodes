class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        
        length = len(rating)
        quantity = 0
        
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if (rating[i] - rating[j]) * (rating[j] - rating[k]) > 0:
                        quantity += 1
        return quantity
        
