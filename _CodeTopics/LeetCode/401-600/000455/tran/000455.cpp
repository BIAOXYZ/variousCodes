class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {

        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int res = 0, i = 0, j = 0;
        while (i < g.size() && j < s.size()) {
            if (s[j] >= g[i]) {
                res++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return res;

    }
};

/*
https://leetcode-cn.com/submissions/detail/133600798/

21 / 21 个通过测试用例
状态：通过
执行用时: 80 ms
内存消耗: 17.3 MB

执行用时：80 ms, 在所有 C++ 提交中击败了92.30%的用户
内存消耗：17.3 MB, 在所有 C++ 提交中击败了74.06%的用户
*/
