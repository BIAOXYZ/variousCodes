
/*
超时后打算用 C++ 写。写到 small 那里，发现原来是二分的左半边移动的不对。。。然后直接回 Python 改去了。
*/

class Solution {
public:
    int maximumCandies(vector<int>& candies, long long k) {
        
        int n = candies.size();
        sort(candies);
        
        int res = 0;
        int small = 0, big = candies.back();
        int mid = -1, total = 0;
        while (small <= big) {
            mid = small + (big - small) / 2;
            if (mid == 0)
                break;
            for (int candy : candies)
                total += candy /mid;
            if (total < k)
                big = mid - 1;
            else if (total >= k)
                res = max(res, mid)
                small
        } 
    }
};
