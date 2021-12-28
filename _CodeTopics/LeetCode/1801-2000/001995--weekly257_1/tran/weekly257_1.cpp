class Solution {
public:
    int countQuadruplets(vector<int>& nums) {
        
        // 第 257 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/215306858/

        size_t n = nums.size();
        int res = 0;
        for (int i = 0; i < n-3; ++i)
            for (int j = i+1; j < n-2; ++j)
                for (int k = j+1; k < n-1; ++k)
                    for (int l = k+1; l < n; ++l)
                        if (nums[i] + nums[j] + nums[k] == nums[l])
                            res += 1;
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/252974411/

执行用时：128 ms, 在所有 C++ 提交中击败了62.37%的用户
内存消耗：10.2 MB, 在所有 C++ 提交中击败了50.00%的用户
通过测试用例：
211 / 211
*/
