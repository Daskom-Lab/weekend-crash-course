#include<stdio.h>

int main(int argc, char const *argv[])
{
    int a, *b;
    a = 5;
    b = &a;
    *b = 7;
    printf("a = %d\n", a);
    printf("b = %d\n", b);

    printf("address a = %d\n", &a);
    printf("address b = %d", &b);
    return 0;
}
