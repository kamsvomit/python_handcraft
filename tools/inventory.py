import time

# --- GUDANG DATA (Global) ---
pangan = ["beras", "gula", "sayur"]
stok_pangan = [10, 10, 10]

# --- MESIN 1: LOGIN ---
def login():
    user_list = ["admin", "pawang"]
    pwd_list = [123, 456]
    print("=== PINTU MASUK SISTEM GHAIB ===")
    while True:
        user = input("Username: ")
        pas = int(input("Password: "))
        if (user, pas) in list(zip(user_list, pwd_list)):
            print("✅ Login Berhasil! Selamat datang, Beb.")
            return True
        print("❌ Login Gagal! Coba lagi.")

# --- MESIN 2: CEK STOK ---
def cek_stok():
    print("\n--- STATUS STOK SAAT INI ---")
    for b, s in zip(pangan, stok_pangan):
        status = "AMAN" if s >= 5 else "GAWAT"
        print(f"📦 {b}: {s} ({status})")
    time.sleep(2)

# --- MESIN 3: TAMBAH STOK ---
def tambah_stok():
    barang = input("Masukkan nama barang yang mau ditambah: ").lower()
    if barang in pangan:
        idx = pangan.index(barang)
        jumlah = int(input(f"Mau tambah berapa {barang}?: "))
        stok_pangan[idx] += jumlah
        print(f"✅ Stok {barang} berhasil ditambah!")
    else:
        print("❌ Barang gak ada di list, Beb.")

# --- MESIN 4: KURANG STOK ---
def kurang_stok():
    barang = input("Masukkan nama barang yang berkurang: ").lower()
    if barang in pangan:
        idx = pangan.index(barang)
        jumlah = int(input(f"Kurang berapa {barang}?: "))
        if stok_pangan[idx] >= jumlah:
            stok_pangan[idx] -= jumlah
            print(f"✅ Stok {barang} berhasil dikurangi!")
        else:
            print("❌ Stok gak cukup buat dikurangi segitu!")
    else:
        print("❌ Barang gak ada, Beb.")

# --- MESIN INDUK (TOMBOL ANALOG) ---
def menu_utama():
    if login(): # Hanya jalan kalau login True
        while True:
            print("\n===== PANEL KONTROL INVENTORY =====")
            print("1. Cek Semua Stok")
            print("2. Tambah Stok (Barang Masuk)")
            print("3. Kurang Stok (Barang Keluar)")
            print("4. Logout & Keluar")
            
            pilihan = input("Pencet Nomor Mesin (1-4): ")
            
            if pilihan == "1":
                cek_stok()
            elif pilihan == "2":
                tambah_stok()
            elif pilihan == "3":
                kurang_stok()
            elif pilihan == "4":
                print("Sistem Shutdown... Bye Beb! 😴")
                break
            else:
                print("Tombol salah! Fokus, Beb!")

# --- EKSEKUSI POWER ---
menu_utama()
