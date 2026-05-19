# API CONTRACT

---

## GET /api/profile

### Response

```json
{
  "id": 1,
  "username": "suryanadhif",
  "email": "user@mail.com"
}
```

---

## POST /api/login

### Request

```json
{
  "email": "user@mail.com",
  "password": "123456"
}
```

### Response

```json
{
  "status": "success",
  "token": "jwt_token"
}
```

---

## POST /api/register

### Request

```json
{
  "username": "suryanadhif",
  "email": "user@mail.com",
  "password": "123456"
}
```

### Response

```json
{
  "status": "success",
  "message": "Registrasi berhasil"
}
```

---

## GET /api/posts

### Response

```json
[
  {
    "id": 1,
    "title": "Posting Pertama"
  }
]
```

---

## POST /api/posts

### Request

```json
{
  "title": "Judul Post",
  "content": "Isi posting"
}
```

### Response

```json
{
  "status": "success",
  "message": "Post berhasil dibuat"
}
```