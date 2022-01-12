class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        
        if (nums.size() == 1)
            return 0;
        
        vector<int> numsCopy(nums); 
        std::sort(numsCopy.begin(), numsCopy.end());
        
        int maxNum = numsCopy.back(), secondMaxNum = numsCopy[nums.size()-2];
        int maxNumInd = find(nums.begin(), nums.end(), maxNum) - nums.begin();
        return maxNum >= 2 * secondMaxNum ? maxNumInd : -1;
    }
};

/*
https://leetcode-cn.com/submissions/detail/257871664/

执行用时：4 ms, 在所有 C++ 提交中击败了58.22%的用户
内存消耗：10.7 MB, 在所有 C++ 提交中击败了17.37%的用户
通过测试用例：
232 / 232
*/
