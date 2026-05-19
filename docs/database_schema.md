# Database Schema

## Tabel users

| Field | Type | Keterangan |
|---|---|---|
| id | integer | Primary Key |
| username | varchar | Nama pengguna |
| email | varchar | Email pengguna |
| password | varchar | Password terenkripsi |


## Tabel posts

| Field | Type | Keterangan |
|---|---|---|
| id | integer | Primary Key |
| user_id | integer | Relasi ke users |
| title | varchar | Judul posting |
| content | text | Isi posting |
