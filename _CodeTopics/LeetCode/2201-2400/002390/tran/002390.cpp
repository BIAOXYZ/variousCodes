#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // 包含 std::reverse

class Solution {
public:
    string removeStars(string s) {

        // https://leetcode.cn/problems/removing-stars-from-a-string/submissions/564536744/

        int n_undeleted = 0;
        vector<char> res_lis;

        // 反向遍历字符串，有一个星号，就说明最近的一个非星号字符需要删除。
        std::reverse(s.begin(), s.end());
        for (char ch : s) {
            if (ch == '*') {
                n_undeleted++;
            } else {
                if (n_undeleted > 0) {
                    n_undeleted--;
                } else {
                    res_lis.push_back(ch);
                }
            }
        }

        for (int i = 0; i < n_undeleted; ++i) {
            res_lis.push_back('*');
        }
        // 也可以使用 insert 方法添加未删除的星号
        // res_lis.insert(res_lis.end(), n_undeleted, '*');

        // 另一种反转方式，不过这里是反转 list 然后生成字符串
        std::string res(res_lis.rbegin(), res_lis.rend());
        return res;
    }
};

/*
https://leetcode.cn/problems/removing-stars-from-a-string/submissions/565847925?envType=daily-question&envId=2024-09-14

通过
零知识证明
零知识证明
提交于 2024.09.18 20:43

执行用时分布
68
ms
击败
96.43%

消耗内存分布
26.46
MB
击败
84.66%
*/
