#include<stdio.h>
#include<stdbool.h>
#define a printf
#define b "Daskom1337"
// main() {a(b);}

main(){
// Real code (70 bytes)
char c = getchar();
if(c=='Y') {
    a("Yes");
} else {
    a("No");
}

// Golfed code (29 bytes)
a(getchar()=='Y'?"Yes":"No");
}