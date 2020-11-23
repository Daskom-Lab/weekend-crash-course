#include<stdio.h>

int main(int argc, char const *argv[])
{
    FILE *fp;

    char nama[3][10] = {"fakhri", "test", "lagi"};

    fp = fopen("test.txt", "w+");
    fwrite(nama, 10, 3, fp);
    char test[20];
    fflush(fp);
    fwrite(nama, 10, 3, fp);
    fclose(fp);
    // fread(test, 20, 1, fp);
    // printf("output = %s", test);

    return 0;
}