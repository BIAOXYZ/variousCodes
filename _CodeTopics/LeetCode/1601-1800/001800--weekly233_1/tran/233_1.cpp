class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {

        // 第 233 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/157773120/

        int n = nums.size();
        if (n == 1) 
            return nums[0];
        
        int res = nums[0], currMax = nums[0];
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i-1]) {
                currMax += nums[i];
            } else {
                res = max(res, currMax);
                currMax = nums[i];
            }
        }
        res = max(res, currMax);
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/370476122/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
40.06%
的用户
内存消耗：
8.2 MB
, 在所有 C++ 提交中击败了
45.24%
的用户
通过测试用例：
104 / 104
*/
