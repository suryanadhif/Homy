# Database Schema

## Tabel users

| Field | Type | Keterangan |
|---|---|---|
| id | integer | Primary Key |
| username | varchar | Nama pengguna |
| email | varchar | Email pengguna |
| password | varchar | Password terenkripsi |


## Tabel properties

| Field | Type | Keterangan |
|---|---|---|
| id | integer | Primary Key |
| user_id | integer | Relasi ke users |
| title | varchar | Nama properti |
| location | varchar | Lokasi properti |
| price | decimal | Harga properti |
| description | text | Deskripsi properti |
| image_url | text | Foto properti |