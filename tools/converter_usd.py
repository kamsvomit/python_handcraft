# mesin hitung kurs USD ke Rupiah

def kurs(usd):
    rate = 16835
    hitung = rate * usd
    return hitung

print("=====selamat datang di mesin kurs usd=====")

usd_input = float(input("masukan nilai usd: "))

nilai = kurs(usd_input)

print(f"nilai dalam rupiah : {nilai}")