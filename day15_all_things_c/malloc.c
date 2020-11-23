#include<stdio.h>
#include<stdlib.h>

int main(int argc, char const *argv[])
{
    char *nama;

    nama = (char *) malloc(100);
    nama = "test";
    // nama = (char *) realloc(nama, 120);
    printf("%s", nama);

    return 0;
}
