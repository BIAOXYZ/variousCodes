class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {

        // https://leetcode.cn/problems/merge-sorted-array/submissions/164116933/
        for (int i = 0; i < n; ++i) {
            nums1[i+m] = nums2[i];
        }
        std::sort(nums1.begin(), nums1.end());
    }
};
/*
https://leetcode.cn/problems/merge-sorted-array/submissions/455944471/

时间
详情
-ms
击败 100.00%使用 C++ 的用户
内存
详情
8.61mb
击败 48.88%使用 C++ 的用户
*/
/*
现在时间太短的话不是 0ms 了，是直接不显示时间了。
*/
