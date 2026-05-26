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

## GET /api/properties

### Response

```json
[
  {
    "id": 1,
    "title": "Rumah Minimalis",
    "location": "Jakarta",
    "price": 500000000
  }
]
```

---

## POST /api/properties

### Request

```json
{
  "title": "Rumah Modern",
  "location": "Bandung",
  "price": 750000000,
  "description": "Rumah modern 2 lantai"
}
```

### Response

```json
{
  "status": "success",
  "message": "Post berhasil dibuat"
}
```