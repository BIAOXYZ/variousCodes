#if 0

/* lower���� c ת��ΪСд��ʽ���������� ASCII �� */
int lower(int c)
{
    if (c >= 'A' && c <= 'Z')
        return c + 'a' �C 'A';
    else
        return c;
}

#endif // 0



/* ����������ԭ������ӣ�û���������϶���û�����еġ�
���Ǽ����������Լ������º��ˡ�*/


int lower(int c)
{
    if (c >= 'A' && c <= 'Z')
        return c + 'a' �C 'A';
    else
        return c;
}


/* ���Ա�׼ͷ�ļ� <ctype.h>�е�tolower()������isdigit()���� */


