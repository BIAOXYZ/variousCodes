#include <vector>
#include <algorithm>

class Solution {
public:
    int maxNumOfMarkedIndices(vector<int>& nums) {
        
        // https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/submissions/563984418

        int n = nums.size();
        if (n == 1)
            return 0;

        int ptr_small = 0;
        int ptr_large = n / 2 + (n & 1);

        std::sort(nums.begin(), nums.end());
        int res = 0;
        while (ptr_large <= n - 1) {
            if (nums[ptr_small] * 2 <= nums[ptr_large]) {
                res += 2;
                ptr_small++;
            }
            ptr_large++;
        }
        return res;
    }
};

/*
https://leetcode.cn/problems/find-the-maximum-number-of-marked-indices/submissions/564166178

通过
零知识证明
零知识证明
提交于 2024.09.12 21:37

执行用时分布
121
ms
击败
65.05%
消耗内存分布
62.47
MB
击败
40.86%
*/
