# DESIGN DOCUMENT - HOMY

## Deskripsi Aplikasi

Homy adalah platform digital jual beli dan pencarian properti yang dirancang untuk membantu pengguna menemukan rumah dengan mudah, cepat, dan efisien.

Aplikasi menyediakan fitur pencarian properti berdasarkan lokasi, tipe rumah, dan rentang harga. Pengguna juga dapat melakukan login, menyimpan properti favorit, dan menghubungi penjual secara langsung.

---

# Tujuan Sistem

- Mempermudah proses pencarian properti
- Menyediakan informasi rumah secara lengkap
- Membantu pengguna membandingkan properti
- Menyediakan dashboard properti modern dan responsif

---

# Arsitektur Sistem

Proyek menggunakan pola arsitektur MVC (Model View Controller).

## Model
Mengelola data pengguna dan properti.

## View
Menampilkan antarmuka pengguna seperti landing page, login, dan dashboard.

## Controller
Menghubungkan view dengan data dan logika bisnis aplikasi.

---

# Struktur Folder

```text
controllers/
models/
views/
docs/
```

---

# Desain UI

Mockup UI mencakup:

- Landing Page
- Login/Register Page
- Dashboard Sebelum Login
- Dashboard Sesudah Login

Dokumentasi UI:
- ui_mockup.md
- docs/ui_components.md

---

# Link Mockup UI

Canva:
https://www.canva.com/design/DAHKK2rsuJM/j_87rsPQeWNTDQnC3YwFcg/edit

# API Contract

Endpoint utama sistem:

1. GET /api/profile
2. POST /api/login
3. POST /api/register
4. GET /api/posts
5. POST /api/posts

Dokumentasi API:
- docs/api_contract.md

---

# Database Schema

Database utama menggunakan tabel:

- users
- posts

Dokumentasi database:
- docs/database_schema.md

---

# Teknologi yang Digunakan

## Frontend
- HTML
- CSS

## Backend
- Python

## Version Control
- Git
- GitHub

---

# Status Pengembangan

Saat ini proyek masih berada pada fase desain sistem dan dokumentasi awal sebelum implementasi penuh aplikasi dilakukan.