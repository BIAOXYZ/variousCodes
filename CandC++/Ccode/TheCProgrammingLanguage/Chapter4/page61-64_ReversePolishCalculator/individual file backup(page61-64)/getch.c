#define BUFSIZE 100

char buf[BUFSIZE];  /* 供 unget 函数使用的缓冲区 */
int bufp = 0;       /* buf 中的下一个空闲位置 */

int getch(void)     /* 取一个字符（可能是压回的字符） */
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) /* 将字符压回到输入中 */
{
    if (bufp >= BUFSIZE)
        printf("ungetch: 压回字符过多\n");
    else
        buf[bufp++] = c;
}
