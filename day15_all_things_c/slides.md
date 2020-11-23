---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://github.com/Daskom-Lab/weekend-crash-course/raw/master/template-bg.png')
marp: true
---

<style>
section::after {
  font-weight: bold;
  font-size: 0.6em;
  text-shadow: 1px 1px 0 #fff;
  margin-right: 8px;
  margin-bottom: 6px;
  content: 'Page ' attr(data-marpit-pagination);
}

section.stretch-pad {
  padding-top: 40px;
  padding-right: 45px;
  padding-left: 45px;
}

</style>
<!-- _paginate: false -->

# All things **C**

You gotta C me rolling 🤟🏽

---

```c
#include<stdio.h>
int main(int argc, char *argv[]) {
    printf("Name = Muhammad Fakhri Putra Supriyadi");
    printf("      \n\
         _   _ _  \n\
        | | | (_) \n\
        | |_| | | \n\
        |  _  | | \n\
        |_| |_|_| \n\
    ");
    return 1337;
}
```

---

# C / C++ / C#

C = Simple and Aesthetically danger
C++ = OOP(s), its C but better
C# = Its Java but C

[Good article from csharp-station.com](https://csharp-station.com/understanding-the-differences-between-c-c-and-c/) untuk pemahaman lebih.

---

## Mari kita fokus ke C

- System programming
- Dekat kepada perangkat keras
- Mudah untuk mengontrol memori
- Syntax cukup sederhana

---
<!-- _class: stretch-pad -->

## Struktur kode

```c
// Ini merupakan tempat menyimpan library
#include<blablabla>

// Disini bisa kita simpan variabel global
int c = 1;

// Ini tempat menyimpan seluruh kodingan
int main() {

  // Disini isi dari kodingan pada 
  // fungsi main (fungsi utama)
  int a = 0;
  return a;
}
```

---

## Compilers

Sebenarnya ada banyak sekali compilernya, bisa dilihat [disini](https://en.wikipedia.org/wiki/List_of_compilers#C_compilers).

Tetapi yang paling terkenal adalah **GCC**, karena open-source dan support banyak bahasa dan arsitektur.

**MingW** = Porting GCC untuk OS Microsoft Windows.

---

## Debuggers

Debugger dibutuhkan untuk tentunya men-debug sebuah aplikasi / program dalam artian mencek apa yang terjadi pada program saat program dijalankan.

**GDB** = GNU Debugger.

Atau bisa juga gunakan debugger yang lebih user friendly contohnya [debugger pada visual studio code](https://code.visualstudio.com/docs/languages/cpp).

---

## Lets talk about code

Tidak semua kode melainkan hanya beberapa hal penting yang harus dibahas dan dipahami untuk pemahaman C yang bagus.

- Struct, Typedef, Union, Enum
- Pointers
- File(s)
- Malloc / Calloc

---

## Struct 

Digunakan untuk membuat sebuah variable yang bentukannya menyesuaikan keinginan sendiri.

---

## Typedef

Digunakan sebagai alias dari sebuah bentuk tipe data yang sudah dibuat sebelumnya (terutama agar memudahkan pembacaan kode).

Source yang bagus = https://aticleworld.com/typedef-in-c/

---

## Union 

Sama halnya dengan `struct` hanya saja memori yang teralokasikan hanyalah sebesar size terbesar dari variable yang terdapat didalamnya.

Source yang bagus = https://aticleworld.com/union-in-c/

---

## Enum

Mirip dengan `macro`, akan tetapi pembacaan kode akan jauh lebih mudah sehingga dapat mempermudah saat debugging dan lainnya.

Source yang bagus = https://aticleworld.com/seven-important-points-enum-c-language/

---

## Pointers

Sederhananya, `pointer` hanyalah sebuah penunjuk dalam bentuk `address` pada memori kepada sebuah nilai dari sebuah variable.

---

#### File(s)

Ada dua jenis file yaitu:
- Text file (.txt)
- Binary file (.bin / ataupun dalam ekstensi lainnya) 

Mode operasinya juga beragam:
- r(+), rb(+)
- w(+), wb(+)
- a(+), ab(+)

---

## Malloc / Calloc

`malloc` berguna untuk mengalokasikan memori tanpa menginisialisasi terlebih dahulu isi dari memori yang dialokasikan.

Kebalikkannya, `calloc` mengalokasi serta menginisialisasikan memori nya dengan `0`.

---

# Thanks

Terimakasih dan saya mohon maaf bila ada kesalahan...

Seperti biasa yang buruk datangnya dari saya dan yang baik hanya dari-Nya.