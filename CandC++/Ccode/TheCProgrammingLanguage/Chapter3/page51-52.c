#if 0

/* itoa���� n ת��Ϊ�ַ���ʽ��ŵ� s �� */
void itoa(int n, char s[])
{
    int i, sign;

    if ((sign = n) < 0)  /* ��¼���� */
        n = -n;         /* ʹ n ��Ϊ���� */
    i = 0;
    do {            /* �Է�������������� */
        s[i++] = n % 10 + '0';  /* �õ���һ���� */
    } while ((n /= 10) > 0);    /* ɾ������ */
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}

#endif // 0


/* itoa���� n ת��Ϊ�ַ���ʽ��ŵ� s �� */
void itoa(int n, char s[])
{
    int i, sign;

    if ((sign = n) < 0)  /* ��¼���� */
        n = -n;         /* ʹ n ��Ϊ���� */
    i = 0;
    do {            /* �Է�������������� */
        s[i++] = n % 10 + '0';  /* �õ���һ���� */
    } while ((n /= 10) > 0);    /* ɾ������ */
    if (sign < 0)
        s[i++] = '-';
    s[i] = '\0';
    reverse(s);
}
