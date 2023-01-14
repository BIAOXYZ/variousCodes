class Solution {
public:
    int minMaxGame(vector<int>& nums) {

        // 第 296 场周赛第一题
        // https://leetcode.cn/submissions/detail/321743251/

        int n = nums.size();
        if (n == 1) {
            return nums[0];
        }

        vector<int> newNums(n/2, -1);
        for (int i = 0; i < n/2; ++i) {
            // TODO: 艹，这行的条件换成 if (i & 1 == 0) 就不对，日了！ 
            if (i % 2 == 0) {
                newNums[i] = min(nums[2*i+1], nums[2*i]);
            } else {
                newNums[i] = max(nums[2*i+1], nums[2*i]);
            }
        }
        int res = minMaxGame(newNums);
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/395344528/

执行用时：
8 ms
, 在所有 C++ 提交中击败了
54.88%
的用户
内存消耗：
9.7 MB
, 在所有 C++ 提交中击败了
22.79%
的用户
通过测试用例：
96 / 96
*/
