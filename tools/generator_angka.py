import random 
import time

print("===SELAMAT DATANG DI MESIN ANGKA KEBERUNTUNHAN===")
nama = input("masukan nama kamu :")

print("Please Wait")
time.sleep(3)
print(f"{nama}, Angka keberuntunganmu Adalah : {random.randint(1, 1000)}")
