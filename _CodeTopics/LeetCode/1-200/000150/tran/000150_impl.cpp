class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        stack<int> stk;
        for (string& tk : tokens) {
            if (stk.empty() \ 
                || (tk.length() == 1 && isdigit(tk[0])) \ 
                || (tk.length() > 1 && isdigit(tk[1])) ) {
                stk.push(atoi(tk.c_str()));
            } else {
                // 不能直接写  int rightNum = stk.pop(); 会报如下错误：
                //  error: cannot initialize a variable of type 'int' with an rvalue of type 'void'
                // 就是因为C++ STL里的 stack pop函数是没有返回值的- -
                int rightNum = stk.top(); stk.pop();
                int leftNum = stk.top(); stk.pop();
                if (tk[0] == '+') stk.push(leftNum + rightNum);
                else if (tk[0] == '-') stk.push(leftNum - rightNum);
                else if (tk[0] == '*') stk.push(leftNum * rightNum);
                else if (tk[0] == '/') stk.push(leftNum / rightNum);
            }
        }
        return stk.top();
    }
};

/*
https://leetcode-cn.com/submissions/detail/157481375/

20 / 20 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 11.6 MB

执行用时：12 ms, 在所有 C++ 提交中击败了79.00%的用户
内存消耗：11.6 MB, 在所有 C++ 提交中击败了62.76%的用户
*/
