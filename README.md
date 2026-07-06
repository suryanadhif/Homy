# Homy

## Anggota

1. Surya Nadhif
2. Kayla Amirul Alma

## Role

- Surya Nadhif : Product Lead & Backend Developer
- Kayla Amirul Alma : Frontend Developer

---

# Deskripsi

Homy merupakan website jual beli rumah yang bertujuan untuk memudahkan pengguna dalam mencari dan menjual properti secara online.

---

# Requirements

- Docker Desktop
- Docker Compose
- Git

---

# Cara Install

Clone repository

```bash
git clone https://github.com/suryanadhif/Homy.git
```

Masuk ke folder project

```bash
cd Homy
```

---

# Environment Variables

Salin template environment

```bash
cp env.production.template .env
```

Kemudian sesuaikan nilai:

```
DB_HOST=
DB_PORT=
POSTGRES_PASSWORD=
API_URL=
```

---

# Menjalankan Aplikasi (Docker Compose)

```bash
docker compose -f docker-compose.prod.yml up -d
```

Menghentikan aplikasi

```bash
docker compose -f docker-compose.prod.yml down
```

Melihat status container

```bash
docker ps
```

---

# Production Images

Backend

```
ghcr.io/suryanadhif/homy-be:v1.0.0
```

Frontend

```
ghcr.io/suryanadhif/homy-fe:v1.0.0
```

---

# API Endpoints

| Method | Endpoint | Deskripsi |
|---------|----------|-----------|
| GET | /api/data | Mengambil data rumah |

> Tambahkan endpoint lain apabila memang ada pada `server.py`.

---

# Struktur Project

```
controllers/
docs/
models/
views/
Dockerfile.backend
Dockerfile.frontend
docker-compose.yml
docker-compose.prod.yml
server.py
```

---

# Dokumentasi

Dokumentasi tambahan tersedia pada folder

```
docs/
```
