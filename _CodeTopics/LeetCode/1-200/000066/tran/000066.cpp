class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {

        // https://leetcode-cn.com/submissions/detail/77876194/

        int length = digits.size();
        bool breakflag = false;
        for (int i = length - 1; i > -1; --i) {
            if (digits[i] == 9)
                digits[i] = 0;
            else {
                digits[i]++;
                breakflag = true;
                break;
            }
        }
        if (breakflag) 
            return digits;
        else {
            std::vector<int>::iterator pos = digits.begin();
            digits.insert(pos, 1);
            return digits;
        }
    }
};

/*
https://leetcode-cn.com/submissions/detail/230821902/

111 / 111 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 8.5 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：8.5 MB, 在所有 C++ 提交中击败了72.71%的用户
*/
