#if 0

/* �����ԭʼ�������������������֧Ʊ�����㣩�и��������������
������ÿ�ζ���һ������ÿ��һ����������ǰ����ܴ��������ţ���
������Щ������һ�𣬲���ÿ������֮�󽫵�ǰ���ܺʹ�ӡ������*/

#include <stdio.h>

#define MAXLINE 100

/* ԭʼ������ */
main()
{
    double sum, atof(char []);
    char line[MAXLINE];
    int getline(char line[], int max);

    sum = 0;
    while (getline(line, MAXLINE) > 0)
        printf("\t%g\n", sum += atof(line));
    return 0;
}

#endif // 0



/* �����ԭʼ�������������������֧Ʊ�����㣩�и��������������
������ÿ�ζ���һ������ÿ��һ����������ǰ����ܴ��������ţ���
������Щ������һ�𣬲���ÿ������֮�󽫵�ǰ���ܺʹ�ӡ������*/

#include <stdio.h>

#define MAXLINE 100

/* ԭʼ������ */
main()
{
    double sum, atof(char []);
    char line[MAXLINE];
    int getline(char line[], int max);

    sum = 0;
    while (getline(line, MAXLINE) > 0)
        printf("\t%g\n", sum += atof(line));
    return 0;
}
