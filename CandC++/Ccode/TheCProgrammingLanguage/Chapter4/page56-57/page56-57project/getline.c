#include <stdio.h>  // 这里因为用到了getchar()，所以stdio.h头文件必须被包含进来。

/* getline：取一行放到 s 中，并返回该行的长度 */
int getline(char s[], int lim)
{
    int c, i;

    i = 0;
    while (--lim > 0 && (c = getchar()) != EOF && c != '\n')
        s[i++] = c;
    if (c == '\n')
        s[i++] = c;
    s[i] = '\0';
    return i;
}
