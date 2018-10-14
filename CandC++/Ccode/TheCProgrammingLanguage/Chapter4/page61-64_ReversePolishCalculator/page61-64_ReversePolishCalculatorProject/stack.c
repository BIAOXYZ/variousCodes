#define MAXVAL 100  /* 栈 val 的最大深度 */

int sp = 0;         /* 栈的下一个空闲位置*/
double val[MAXVAL]; /* 存放值的栈 */

/* push：把 f 压入栈中 */
void push(double f)
{
    if (sp < MAXVAL)
        val[sp++] = f;
    else
        printf ("error: 栈满，不能将%g 压栈\n", f);
}

/* pop：弹出并返回栈顶的值 */
void pop(void)
{
    if (sp > 0)
        return val[--sp];
    else {
        printf ("error: 栈空\n");
        return 0.0;
    }
}
