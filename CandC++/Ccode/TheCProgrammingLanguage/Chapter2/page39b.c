#if 0

void strcat(char s[], char t[])
{
    int i, j;

    i = j = 0;
    while (s[i] != '\0')    /* 找到 s 的末尾 */
        i++;
    while ((s[i++] = t[j++]) != '\0') /* 复制 t */
        ;
}

#endif // 0


/* strcat：将 t 拼接到 s 的末尾； s 必须够大 */
void strcat(char s[], char t[])
{
    int i, j;

    i = j = 0;
    while (s[i] != '\0')    /* 找到 s 的末尾 */
        i++;
    while ((s[i++] = t[j++]) != '\0') /* 复制 t */
        ;
}
