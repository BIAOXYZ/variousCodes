class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {

        int length = nums.size();
        std::sort(nums.begin(), nums.end());
        int i = 0;
        while (i < length && nums[i] < 0 && k > 0) {
            nums[i] = -nums[i];
            ++i;
            --k;
        }

        if (k == 0)
            return std::accumulate(nums.begin(), nums.end(), 0);
        else if (k % 2 == 0)
            return std::accumulate(nums.begin(), nums.end(), 0);
        else
            return std::accumulate(nums.begin(), nums.end(), 0) - *std::min_element(nums.begin(), nums.end()) * 2;
    }
};

/*
https://leetcode-cn.com/submissions/detail/244732428/

执行用时：4 ms, 在所有 C++ 提交中击败了90.00%的用户
内存消耗：8.9 MB, 在所有 C++ 提交中击败了17.77%的用户
通过测试用例：
80 / 80
*/
