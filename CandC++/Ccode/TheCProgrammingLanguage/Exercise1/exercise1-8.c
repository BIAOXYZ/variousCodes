/* ��ϰ 1-8. дһ������ͳ�������еĿո��Ʊ���ͻ��з��ĸ�����*/

#include <stdio.h>

int main()
{
    int nSpace, nTab, nLine;
    nSpace = nTab = nLine = 0;
    // int nSpace = nTab = nLine = 0;
    /* ����ֱ����"int nSpace = nTab = nLine = 0;"��䣬�������������Ǹ�ֵ�������ԣ�
    ��һ��ֱ��������������������ʼ��������ʾnTab��nLine��û�����ؾ�ֱ�Ӹ�ֵ�ˡ�
    ��һ��������������������������丳ֵ�ɣ��ֻ�˵nSpace�ظ������ˣ�����ΪnSpaceǰ���int������������Ϊ��������������*/
    int c;

    while ( (c = getchar()) != EOF ){
        if (c == ' ')
            nSpace++;
        else if (c == '\t')
            nTab++;
        else if (c == '\n')
            nLine++;
    }
    printf("The number of spaces, tabs and lines are:\n\tSpace = %d, Tab = %d, Line = %d", nSpace, nTab, nLine);
    return 0;
}
