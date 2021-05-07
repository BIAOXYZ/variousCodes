class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> res(1, first);
        for (auto elem : encoded) {
            res.push_back(elem ^ res[res.size()-1]);
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/175234004/

76 / 76 个通过测试用例
状态：通过
执行用时: 40 ms
内存消耗: 25.5 MB

执行用时：40 ms, 在所有 C++ 提交中击败了27.00%的用户
内存消耗：25.5 MB, 在所有 C++ 提交中击败了5.50%的用户
*/
/*
这个比前一个效率低，肯定是有原因的。
*/
