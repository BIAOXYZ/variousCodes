#if 0

void strcat(char s[], char t[])
{
    int i, j;

    i = j = 0;
    while (s[i] != '\0')    /* �ҵ� s ��ĩβ */
        i++;
    while ((s[i++] = t[j++]) != '\0') /* ���� t */
        ;
}

#endif // 0


/* strcat���� t ƴ�ӵ� s ��ĩβ�� s ���빻�� */
void strcat(char s[], char t[])
{
    int i, j;

    i = j = 0;
    while (s[i] != '\0')    /* �ҵ� s ��ĩβ */
        i++;
    while ((s[i++] = t[j++]) != '\0') /* ���� t */
        ;
}
