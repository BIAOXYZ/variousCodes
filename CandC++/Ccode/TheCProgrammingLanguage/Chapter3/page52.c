#if 0

/* trim：删除字符串末尾的空格、制表符和换行符 */
int trim(char s[])
{
    int n;

    for (n = strlen(s)-1; n >= 0; n--)
        for (s[n] != ' ' && s[n] != '\t' && s[n] != '\n')
            break;
    s[n+1] = '\0';
    return n;
}

#endif // 0

/* trim：删除字符串末尾的空格、制表符和换行符 */
int trim(char s[])
{
    int n;

    for (n = strlen(s)-1; n >= 0; n--)
        if (s[n] != ' ' && s[n] != '\t' && s[n] != '\n') // 很明显这里的for应该是if。
            break;
    s[n+1] = '\0';
    return n;
}
