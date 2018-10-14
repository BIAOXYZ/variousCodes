#include <stdio.h>

#define MAXLINE 1000    /* �������������󳤶� */

int max;                /* ��ǰ������г��� */
char line[MAXLINE];     /* ��ǰ������ */
char longest[MAXLINE];  /* ��ǰ������� */

int getline(void);
void copy(void);

/* ��ӡ��ǰ������У�����汾 */
main()
{
    int len;
    extern int max;
    extern char longest[];

    max = 0;
    while ((len = getline()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)    /* there was a line */
        printf("%s", longest);
    return 0;
}

/* getline������汾 */
int getline(void)
{
    int c, i;
    extern char line[];

    for (i = 0; i < MAXLINE - 1
        && (c=getchar()) != EOF && c != '\n'; ++i)
            line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

/* copy: ����汾 */
void copy(void)
{
    int i;
    extern char line[], longest[];

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}


/* ~~~~~~~~~~�ָ���~~~~~~~~~~ */
/* ���İ��鼮��getline�Ӻ�����forѭ���Ƕ����˸����� */
/* ��Ϊԭ���ĳ�����"�Ǻ�+��б��"���͵�ע�ͱȽ϶࣬
����ֻ����������������*/

/*
ԭ�����
ע��getline�Ӻ��������

for (i = 0; i < MAXLINE - 1
    && (c=getchar)) != EOF && c != '\n'; ++i)

��Ϊ����������ţ��ұ��������ţ����Ա��붼�޷�ͨ�����ҵ�ʱ��һ��Ӧ��ô�ĵģ�

for (i = 0; i < MAXLINE - 1
    && ((c=getchar)) != EOF && c != '\n'; ++i)

������"&&"�������ּ��˸������ţ���������������Ŀ��ƥ���ˣ�����Ҳ�����������ˡ�
�����޷������κ�ֵ����������Ҳ��������getchar����Ҫ��һ�����ŵġ������Ҿ�����
������Ҳ�ܵ���ͨ- -
*/

/* (http://segmentfault.com/q/1010000000449167) */

#if 0

#include <stdio.h>

#define MAXLINE 1000    /* �������������󳤶� */

int max;                /* ��ǰ������г��� */
char line[MAXLINE];     /* ��ǰ������ */
char longest[MAXLINE];  /* ��ǰ������� */

int getline(void);
void copy(void);

/* ��ӡ��ǰ������У�����汾 */
main()
{
    int len;
    extern int max;
    extern char longest[];

    max = 0;
    while ((len = getline()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)    /* there was a line */
        printf("%s", longest);
    return 0;
}

/* getline������汾 */
int getline(void)
{
    int c, i;
    extern char line[];

    for (i = 0; i < MAXLINE - 1
        && (c=getchar)) != EOF && c != '\n'; ++i)
            line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

/* copy: ����汾 */
void copy(void)
{
    int i;
    extern char line[], longest[];

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}

#endif


/*��һ������һ�ĵĽ������ͨ�����룬������cmd���棬�����޷������κ�ֵ��*/

#if 0

#include <stdio.h>

#define MAXLINE 1000    /* �������������󳤶� */

int max;                /* ��ǰ������г��� */
char line[MAXLINE];     /* ��ǰ������ */
char longest[MAXLINE];  /* ��ǰ������� */

int getline(void);
void copy(void);

/* ��ӡ��ǰ������У�����汾 */
main()
{
    int len;
    extern int max;
    extern char longest[];

    max = 0;
    while ((len = getline()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)    /* there was a line */
        printf("%s", longest);
    return 0;
}

/* getline������汾 */
int getline(void)
{
    int c, i;
    extern char line[];

    for (i = 0; i < MAXLINE - 1
        && ((c=getchar)) != EOF && c != '\n'; ++i)
            line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

/* copy: ����汾 */
void copy(void)
{
    int i;
    extern char line[], longest[];

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}

#endif

