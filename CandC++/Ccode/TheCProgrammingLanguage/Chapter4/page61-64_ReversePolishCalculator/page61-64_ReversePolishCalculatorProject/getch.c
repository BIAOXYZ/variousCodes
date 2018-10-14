#define BUFSIZE 100

char buf[BUFSIZE];  /* �� unget ����ʹ�õĻ����� */
int bufp = 0;       /* buf �е���һ������λ�� */

int getch(void)     /* ȡһ���ַ���������ѹ�ص��ַ��� */
{
    return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c) /* ���ַ�ѹ�ص������� */
{
    if (bufp >= BUFSIZE)
        printf("ungetch: ѹ���ַ�����\n");
    else
        buf[bufp++] = c;
}
