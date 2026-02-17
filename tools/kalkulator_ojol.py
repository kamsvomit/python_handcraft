#mesin hitung
def kalkulator_ojol(modal, uang_didapat):
	pendapatan_bersih = uang_didapat - modal
	return pendapatan_bersih
	
#user_input
print("=====selamat datang di kalkulator ojol=====")
m = float(input("masukan jumlah modal:"))
u = float(input("masukan pendapatan hari ini:"))

#eksekusi
hasil = kalkulator_ojol(m, u)
print(f"pendapatan bersih anda saat ini: {hasil}")
#warning jika minus
if hasil < 0:
	print("===pendapatan anda minus===")