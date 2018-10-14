#include <stdio.h>
#define MAXLINE 1000 /* 最大输入行长度 */

int getline(char line[], int maxline);
void copy(char to[], char from[]);

/* 打印最长的输入行 */
main()
{
    int len;    /* 当前行的长度 */
    int max;    /* 已读入的最长行的长度 */
    char line[MAXLINE];     /* 当前输入行 */
    char longest[MAXLINE];  /* 当前最长的文本行 */

    max = 0;
    while ((len = getline(line, MAXLINE)) > 0)
        if (len > max) {
            max = len;
            copy(longest, line);
        }
    if (max > 0) /* 如果存在一行 */
        printf("%s", longest);
    return 0;
}

/* getline: 将一行文本读取到 s 中, 并返回其长度 */
int getline(char s[],int lim)
{
    int c, i;

    for (i=0; i<lim-1 && (c=getchar())!=EOF && c!='\n'; ++i)
        s[i] = c;
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    return i;
}

/* copy: 将 'from' 拷贝到 'to'，假定 to 足够大 */
void copy(char to[], char from[])
{
    int i;

    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;
}
