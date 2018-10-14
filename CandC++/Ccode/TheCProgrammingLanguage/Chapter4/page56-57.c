#include <stdio.h>
#define MAXLINE 1000    /* ��������г��� */

int getline(char line[], int max);
int strindex(char source[], char searchfor[]);

char pattern[] = "ould";    /* �����ҵ�ģʽ */

/* �ҳ�������ģʽ��ƥ����� */
main()
{
    char line[MAXLINE];
    int found = 0;

    while (getline(line, MAXLINE) > 0)
        if (strindex(line, pattern) >= 0) {
            printf("%s", line);
            found++;
        }
    return found;
}

/* getline��ȡһ�зŵ� s �У������ظ��еĳ��� */
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

/* strindex������ t �� s �е�λ�ã���δ�ҵ��򷵻�-1 */
int strindex(char s[], char t[])
{
    int i, j, k;

    for (i = 0; s[i] != '\0'; i++) {
        for (j = i, k = 0; t[k] != '\0' && s[j] == t[k]; j++, k++)
            ;
        if (k > 0 && t[k] == '\0')
            return i;
    }
    return -1;
}


/* ����Ϊ���İ�ԭ������д�getline��������ʱ���˸��ֺ�- -*/

#if 0

#include <stdio.h>
#define MAXLINE 1000    /* ��������г��� */

int getline(char line[], int max)
int strindex(char source[], char searchfor[]);

char pattern[] = "ould";    /* �����ҵ�ģʽ */

/* �ҳ�������ģʽ��ƥ����� */
main()
{
    char line[MAXLINE];
    int found = 0;

    while (getline(line, MAXLINE) > 0)
        if (strindex(line, pattern) >= 0) {
            printf("%s", line);
            found++;
        }
    return found;
}

/* getline��ȡһ�зŵ� s �У������ظ��еĳ��� */
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

/* strindex������ t �� s �е�λ�ã���δ�ҵ��򷵻�-1 */
int strindex(char s[], char t[])
{
    int i, j, k;

    for (i = 0; s[i] != '\0'; i++) {
        for (j = i, k = 0; t[k] != '\0' && s[j] == t[k]; j++, k++)
            ;
        if (k > 0 && t[k] == '\0')
            return i;
    }
    return -1;
}

#endif // 0

#if 0

/* �������� */

Ah Love! could you and I with Fate conspire
To grasp this sorry Scheme of Things entire,
Would not we shatter it to bits -- and then
Re-mould it nearer to the Heart's Desire!

#endif // 0
