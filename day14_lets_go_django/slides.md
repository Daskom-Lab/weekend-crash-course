---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://github.com/Daskom-Lab/weekend-crash-course/raw/master/template-bg.png')
marp: true
---

<style>
section {
  padding-top: 40px;
  padding-right: 45px;
  padding-left: 45px;
}

section::after {
  font-weight: bold;
  font-size: 0.6em;
  text-shadow: 1px 1px 0 #fff;
  margin-right: 8px;
  margin-bottom: 6px;
  content: 'Page ' attr(data-marpit-pagination);
}
</style>

# **Lets go** Django

Create a web application using one of `python` web framework

---

```python
from django.template import Context, Template

profile = """
<div>
    My name is {{ name|title }},
    Im a {{ profession }},
    And my hobbies are {{ hobbies }}.
</div>
"""

name = 'Fakhri [fai] [f4r4w4y]'
profession = 'Programmer, Developer'
hobbies = 'Playing computer or other kind of electronic devices'

template = Template(profile)
context = Context({
  "name": name,
  "profession": profession,
  "hobbies": hobbies
})
template.render(context)
```

---

**Quick disclaimer**

Ini pertama kalinya saya pake django, saya baru mulai pake semenjak buat slide ini, jadi jangan berharap saya tau semuanya.

Disini saya lebih menekankan gimana cara baca dokumentasi sekaligus cara mengimplementasikannya.

---

### Djang-what ?

Django merupakan salah satu web framework yang menggunakan bahasa `python`

Menurut saya, bisa dibilang laravel nya `python`

---

### Why Django ?

What they mention :
- Ridiculously fast.
- Reassuringly secure.
- Exceedingly scalable.

What i also felt :
- So many features
- Builtin admin system

---

Sebenarnya udah ada seri yang sangat bagus di website django-nya langsung https://docs.djangoproject.com/en/3.1/intro/tutorial01/

Maka dari itu, disini saya akan menjelaskan secara sederhananya...

---

### Project

```bash
$ django-admin startproject daskom1337
```

Dengan command diatas kita bisa membuat sebuah project
dan dengan command dibawah kita bisa membuat sebuah aplikasi

```bash
$ python manage.py startapp newapp
```

But whats the difference ?
Project = bisa terdapat beberapa aplikasi
Aplikasi = bisa berada pada beberapa projek

---

### Setup settings.py (env nya django)

```bash
$ python manage.py migrate
```
Command diatas ini digunakan untuk "menjalankan" settings.py nya

Referensi bagus untuk membuat settings.py yang aman dan efisien :
https://agileleaf.com/blog/a-better-way-to-manage-settings-py-in-your-django-projects/

---

### Run server

```bash
$ python manage.py runserver
```

Command ini digunakan untuk menjalankan aplikasi django yang sedang kita buat, sama hal nya dengan `npm run watch` dia akan otomatis reload saat ada save terbaru.

Note: menambahkan file tidak akan men-trigger auto reload nya.

---

### Penjelasan singkat :

- views.py = menyimpan konfigurasi tampilan dan/atau hasil response
- urls.py = menyimpan konfigurasi url
- models.py = menyimpan konfigurasi model database atau struktur data pada tiap tabelnya
- admin.py = menyimpan konfigurasi untuk tampilan dan kontrol admin
- tests.py = menyimpan konfigurasi untuk testing aplikasinya

---

### The rest, just follow the tutorial

---

### Main takeaway

1) Mempelajari framework itu mudah
2) Perkuat pondasi mengenai bahasanya lebih penting dibanding mempelajari framework langsung
3) Dokumentasi itu penting (**DIBACA** BUKAN CUMAN DILIAT)

---

### Bonus stuff

Disini saya akan coba men-demo-kan apa yang terjadi jika terdapat security vulnerability pada aplikasi django yang kita buat.

Yang paling populer dikalangan ctf player dan (mungkin) bug bounty hunter adalah SSTI (Server Side Template Injection)

Let's pop a calculator !!!

---

![width:800px height:500px](https://media.giphy.com/media/l0D76LT6o1jaG2g0M/giphy.gif)

---

### Terimakasih

Mohon maaf bila ada kesalahan dan seperti biasa yang buruk datang dari saya dan yang baik hanya datang dari-Nya.