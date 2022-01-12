class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        
        if (nums.size() == 1)
            return 0;
        
        vector<int> numsCopy(nums); 
        std::sort(numsCopy.begin(), numsCopy.end());
        
        int maxNum = numsCopy.back(), secondMaxNum = numsCopy[nums.size()-2];
        // 也可以不用 distance 函数，而是直接减。
        // int maxNumInd = find(nums.begin(), nums.end(), maxNum) - nums.begin();
        int maxNumInd = distance(nums.begin(), find(nums.begin(), nums.end(), maxNum));
        return maxNum >= 2 * secondMaxNum ? maxNumInd : -1;
    }
};

/*
https://leetcode-cn.com/submissions/detail/257871524/

执行用时：4 ms, 在所有 C++ 提交中击败了58.22%的用户
内存消耗：10.6 MB, 在所有 C++ 提交中击败了60.41%的用户
通过测试用例：
232 / 232
*/
