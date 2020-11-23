#include<stdio.h>
#include<string.h>

int main () {

    typedef struct hewan {
        int kaki;
        int tangan;
        char nama[100];
    } Hewan;

    Hewan anjing;

    typedef union hewan_u {
        int kaki;
        int tangan;
        char nama[100];
    } Hewan_u;

    Hewan_u ayam;

    enum hari {
        senin,
        selasa,
        rabu = 500,
        kamis,
        jumat,
        sabtu,
        minggu
    };

    int day = 0;
    switch (day) {
        case senin:
            printf("senin ...");
            break;
        
        case selasa:
            printf("selasa ...");
            break;

        default:
            break;
    }
}