#include <queue>
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {

        priority_queue<vector<int>> hp;
        // 这里下面那句不行，需要把 nums1.size() 强制类型转换一下 min 才能用。
        // for (int i = 0; i < min(k, nums1.size()); ++i)
        for (int i = 0; i < min(k, (int)nums1.size()); ++i) {
            for (int j = 0; j < min(k, (int)nums2.size()); ++j) {
                // 注意 C++ 的是大根堆，Python是小根堆。
                hp.push(vector<int>{-nums1[i]-nums2[j], nums1[i], nums2[j]});
            }
        }
        
        vector<vector<int>> res;
        while (!hp.empty() && k > 0) {
            vector<int> v = hp.top();
            hp.pop();
            res.push_back(vector<int>(v.begin()+1, v.end()));
            --k;
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/258840151/

执行用时：1872 ms, 在所有 C++ 提交中击败了5.08%的用户
内存消耗：385.7 MB, 在所有 C++ 提交中击败了5.09%的用户
通过测试用例：
32 / 32
*/
