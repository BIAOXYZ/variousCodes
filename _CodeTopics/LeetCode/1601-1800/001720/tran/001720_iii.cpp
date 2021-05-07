class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> res(1, first);
        for (auto elem : encoded) {
            // res[res.size()-1] 也可以换成如下形式： *(res.end()-1)。
            res.push_back(elem ^ *(res.end()-1));
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/175236554/

76 / 76 个通过测试用例
状态：通过
执行用时: 36 ms
内存消耗: 25.3 MB

执行用时：36 ms, 在所有 C++ 提交中击败了47.94%的用户
内存消耗：25.3 MB, 在所有 C++ 提交中击败了42.64%的用户
*/
