#if 0

/* itoa：将 n 转换为字符形式存放到 s 中 */
void itoa(int n, char s[])
{
    int i, sign;

    if ((sign = n) < 0)  /* 记录符号 */
        n = -n;         /* 使 n 变为正数 */
    i = 0;
    do {            /* 以反向次序生成数字 */
        s[i++] = n % 10 + '0';  /* 得到下一个数 */
    } while ((n /= 10) > 0);    /* 删除该数 */
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}

#endif // 0


/* itoa：将 n 转换为字符形式存放到 s 中 */
void itoa(int n, char s[])
{
    int i, sign;

    if ((sign = n) < 0)  /* 记录符号 */
        n = -n;         /* 使 n 变为正数 */
    i = 0;
    do {            /* 以反向次序生成数字 */
        s[i++] = n % 10 + '0';  /* 得到下一个数 */
    } while ((n /= 10) > 0);    /* 删除该数 */
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}
