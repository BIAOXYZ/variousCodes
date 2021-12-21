class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        
        // https://leetcode-cn.com/submissions/detail/250848404/

        int lena = a.size(), lenb = b.size();
        int quotient = lenb / lena;
        int remainder = lenb % lena;
        
        if (remainder == 0)
            quotient += 1;
        else
            quotient += 2;
        std::string A = "";
        for (int i = 0; i < quotient; ++i)
            A += a;
        
        int ind = A.find(b);
        if (ind == std::string::npos) {
            return -1;
        } else {
            if (A.size() - (ind + lenb) >= lena)
                return quotient - 1;
            else
                return quotient;
        }
    }
};

/*
https://leetcode-cn.com/submissions/detail/250850730/

执行用时：4 ms, 在所有 C++ 提交中击败了86.50%的用户
内存消耗：6.7 MB, 在所有 C++ 提交中击败了77.30%的用户
通过测试用例：
57 / 57
*/
