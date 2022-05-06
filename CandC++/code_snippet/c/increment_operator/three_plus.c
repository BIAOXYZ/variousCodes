#include <stdio.h>
int main() {
    int a=2, b=3, c=0;
    // c = a++ + b
    c = a+++b;
    printf("%d%d%d\n",a,b,c);
    
    a = 2;b = 3;c = 0;
    // c = a + b++
    c = a+b++;
    printf("%d%d%d\n",a,b,c);
    
    a = 2;b = 3;c = 0;
    c = (a++)+b;
    printf("%d%d%d\n",a,b,c);
    
    a = 2;b = 3;c = 0;
    c = a+(b++);
    printf("%d%d%d\n",a,b,c);
    
    printf("Let's see some differences!\n");
    
    a = 2;b = 3;c = 0;
    c = a+(++b);
    printf("%d%d%d\n",a,b,c);
    
    a = 2;b = 3;c = 0;
    c = (++a)+b;
    printf("%d%d%d\n",a,b,c);
}

/*
335
245
335
245
Let's see some differences!
246
336
*/
