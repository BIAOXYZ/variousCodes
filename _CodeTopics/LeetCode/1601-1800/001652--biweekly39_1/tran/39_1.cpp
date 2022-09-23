class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {

        // 第 39 场双周赛第一题
        // 	https://leetcode-cn.com/submissions/detail/123458508/

        int length = code.size();
        vector<int> res(length, 0);
        
        if (k == 0) {
            return res;
        } else if (k > 0) {
            for (int i = 0; i < length; ++i) {
                for (int offset = 1; offset < k + 1; ++offset) {
                    res[i] += code[(i + offset) % length];
                }
            }
        } else {
            for (int i = 0; i < length; ++i) {
                for (int offset = -1; offset > k-1; --offset) {
                    // 下面这行要是python里可以，但是 c++ 会有中括号里的数组 index 为负值的问题，
                    // 因此变通一下，先额外加个 length 上去，从而保证一定为正。
                    // res[i] += code[(i + offset) % length];
                    res[i] += code[(i + offset + length) % length];
                }
            }            
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/366523151/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
54.48%
的用户
内存消耗：
8 MB
, 在所有 C++ 提交中击败了
70.76%
的用户
通过测试用例：
74 / 74
*/
