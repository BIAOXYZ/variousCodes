int evalRPN(char ** tokens, int tokensSize){

    int stk[tokensSize];
    memset(stk, 0, sizeof(stk));
    int top = 0;
    for (int i = 0; i < tokensSize; ++i) {
        char* tk = tokens[i];
        //printf("-----index is %d, tk is %s\n", i, tk);
        if ((strlen(tk) == 1 && isdigit(tk[0])) || (strlen(tk) > 1 && isdigit(tk[1]))) {
                stk[top++] = atoi(tk);
                //printf("***index is %d, stk[top-1] is %d, top is %d\n", i, stk[top-1], top);
        } else {
            /*
            // int rightNum = stk[top--];  
            // 这里最开始写成 top--，是不对的，会取到默认值0。。。必须用 --top
            */
            int rightNum = stk[--top];
            int leftNum = stk[--top];
            //printf("===index is %d, leftnum is %d, rightnum is %d\n", i, leftNum, rightNum);
            if (tk[0] == '+') stk[top++] = leftNum + rightNum;
            else if (tk[0] == '-') stk[top++] = leftNum - rightNum;
            else if (tk[0] == '*') stk[top++] = leftNum * rightNum;
            else if (tk[0] == '/') stk[top++] = leftNum / rightNum;
        }
    }
    /* 注意这里一定得是 [top-1]，而不是 [top]，理由和上面类似。*/
    return stk[top-1];
}

/*
https://leetcode-cn.com/submissions/detail/157598282/

20 / 20 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 7 MB

执行用时：8 ms, 在所有 C 提交中击败了92.77%的用户
内存消耗：7 MB, 在所有 C 提交中击败了97.66%的用户
*/
