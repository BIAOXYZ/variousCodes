#if 0

/* atoi：将 s 转换为对应的整数 */
{
    int i, n;

    n = 0;
    for (i = 0; s[i] >= '0' && s[i] <= '9'; ++i)
        n = 10 * n + (s[i] – '0');
    return n;
}

#endif

/* 上面是书上原版的例子，没有主函数肯定是没法运行的。
于是加上主函数自己运行下好了。*/

{
int i, n;
n = 0;
for (i = 0; s[i] >= '0' && s[i] <= '9'; ++i)
n = 10 * n + (s[i] – '0');
return n;
}
