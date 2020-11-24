#include <stdio.h>

void ptr_case1() {
    printf("--------------------Start of Case 1!--------------------\n");
    char *sptr = "abc", *tptr;
    /* warning: assignment makes integer from pointer without a cast [-Wint-conversion] */
    *tptr = sptr;    // Segmentation fault (core dumped)
    printf("--------------------End of Case 1!--------------------\n");
}

void ptr_case2() {
    printf("--------------------Start of Case 2!--------------------\n");
    char *sptr = "abc", *tptr;
    tptr = sptr;
    printf("The string *tptr is: %s\n", tptr);
    printf("The char tptr[2] is: %c\n", *(tptr + 2));
    printf("The char tptr[2] is: %c\n", tptr[2]);
    printf("--------------------End of Case 2!--------------------\n");
}

void ptr_case3() {
    printf("--------------------Start of Case 3!--------------------\n");
    char *sptr = "abc", *tptr;
    *tptr = *sptr;   // Segmentation fault (core dumped)
    printf("--------------------End of Case 3!--------------------\n");
}

void ptr_case4() {
    printf("--------------------Start of Case 4!--------------------\n");
    int *iptr = (int *) 10;
    *iptr = 11;   // Segmentation fault (core dumped)
    printf("--------------------End of Case 4!--------------------\n");
}

void ptr_case5() {
    printf("--------------------Start of Case 5!--------------------\n");
    /* warning: initialization makes pointer from integer without a cast [-Wint-conversion] */
    int *iptr = 10;
    *iptr = 11;   // Segmentation fault (core dumped)
    printf("--------------------End of Case 5!--------------------\n");
}

void ptr_case6() {
    printf("--------------------Start of Case 6!--------------------\n");
    int *iptr = (int *) 10;
    iptr = NULL;
    // printf("The int *iptr is: %d\n", *iptr);   // Segmentation fault (core dumped)
    /* warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘int *’ [-Wformat=] */
    printf("The address of iptr in INT form is: %d\n", iptr);
    printf("2nd: The address of iptr in POINTER form is: %p\n", iptr);
    printf("--------------------End of Case 6!--------------------\n");
}

int main()
{
    /* 
     * 只有2和6是完全正确的，不会造成 Segmentation fault (core dumped)。其他四个会使
     * 程序直接退出，所以就注释掉这四个在main里的执行。但是会标出造成段错误的语句。
     */
    //ptr_case1();
    ptr_case2();
    //ptr_case3();
    //ptr_case4();
    //ptr_case5();
    ptr_case6();
    return 0;
}

/******************************************************************************
main.c:7:11: warning: assignment makes integer from pointer without a cast [-Wint-conversion]                           
main.c:38:17: warning: initialization makes pointer from integer without a cast [-Wint-conversion]                      
main.c:49:50: warning: format ‘%d’ expects argument of type ‘int’, but argument 2 has type ‘int *’ [-Wformat=]          
--------------------Start of Case 2!--------------------                                                                
The string *tptr is: abc                                                                                                
The char tptr[2] is: c                                                                                                  
The char tptr[2] is: c                                                                                                  
--------------------End of Case 2!--------------------                                                                  
--------------------Start of Case 6!--------------------                                                                
The address of iptr in INT form is: 0                                                                                   
2nd: The address of iptr in POINTER form is: (nil)                                                                      
--------------------End of Case 6!--------------------
*******************************************************************************/

/*
《Mastering Algorithms with C》
《算法精解：C语言描述》 -- 第2章 指针操作 -- 问与答

问：下列几段代码，哪些会造成编译时错误，哪些会造成运行时错误，为什么？
答：
a）编译时错误。因为*tptr是一个字符，而sptr是一个指向字符的指针，代码试图将一个字符指针赋给一个字符，很显然这会产生类型冲突。
b）没有错误。因为tptr和sptr都是字符指针。
c）可能产生运行时错误。因为程序并没有为tptr分配存储空间。当解引用tptr时，无法确定它的指向。
d）可能产生运行时错误。因为将一个固定的地址赋值给一个整型指针是很危险的。当解引用iptr时，我们会把11写到地址为10的*iptr中，这种操作很可能不合法。
e）可能产生运行时错误或者警告。因为此代码尝试将一个整数赋给一个整型指针，很多时候这种操作并不合法或会造成类型冲突。
f）没有错误。因为，虽然程序一开始做了一个将固定地址赋给整型指针iptr的危险操作，但它立刻将此指针设置为NULL，这是正确的操作。
*/
