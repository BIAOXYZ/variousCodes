#include <stdio.h>

/* �����뿽�������; �汾 2 */
main()
{
    int c;

    while ((c = getchar()) != EOF)
        putchar(c);
}

/*
���� != �����ȼ����� = ������ζ�����û��Բ���ţ��Ƚϲ��� != ���ڸ�ֵ���� = ֮ǰ��ɡ�
������c = getchar() != EOF  �ȼ��� c = (getchar() != EOF)
�������Ǹ��� getchar �ĵ����Ƿ������ļ������������� c ����Ϊ 0 �� 1���Ⲣ��������ϣ
���ﵽ��Ч����
*/

/*
#include <stdio.h>
main()
{
    int c;
    while (c = getchar() != EOF)
        putchar(c);
}
*/
