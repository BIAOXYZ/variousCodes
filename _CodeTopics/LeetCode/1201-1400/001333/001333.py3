class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        restaurants = [restaurant for restaurant in restaurants if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance]
        if veganFriendly:
            restaurants = [restaurant for restaurant in restaurants if restaurant[2] == 1]
        restaurants.sort(key = lambda x : (-x[1], -x[0]))
        return [restaurant[0] for restaurant in restaurants]
        
"""
https://leetcode.cn/problems/filter-restaurants-by-vegan-friendly-price-and-distance/submissions/469906577/?envType=daily-question&envId=2023-09-27

时间
详情
40ms
击败 98.25%使用 Python3 的用户
内存
详情
22.66MB
击败 7.02%使用 Python3 的用户
"""
