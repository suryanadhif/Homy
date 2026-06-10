# Integration Log - Minggu 11

## Hasil Integrasi

Frontend berhasil mengambil data dari Backend menggunakan Fetch API.

Endpoint yang digunakan:

GET /api/data

## Kendala

1. Frontend tidak dapat mengakses asset karena routing Flask belum sesuai.
2. Path gambar dan CSS perlu disesuaikan dengan konfigurasi server.

## Solusi

1. Backend menambahkan routing static file pada Flask.
2. Frontend memperbarui pemanggilan asset.
3. Pengujian ulang dilakukan hingga endpoint dan asset dapat diakses.

## Evaluasi Keamanan CORS

Saat ini CORS menggunakan:

CORS(app,
     resources={
         r"/*": {
             "origins": "http://127.0.0.1:5000"
         }
     })