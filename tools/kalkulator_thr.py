def calculate(masa_kerja, gaji):
    """Perform arithmetic operations"""
    operation = masa_kerja / 12 * gaji
    return operation

def main():
    """Main function to run the calculator"""
    print("=" * 50)
    print("KALKULATOR THR")
    print("=" * 50)
    
    while True:
        try:
            masa_kerja = float(input("\nMasukan Masa Kerja (1-?): "))
            gaji = float(input("Masukan Gaji: "))
            
            result = calculate(masa_kerja, gaji)
            print(f"\nTHR Karyawan Anda Sebesar : {result}")
            
            another = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if another != "yes":
                print("\nThank you for using the calculator!")
                break
                
        except ValueError:
            print("Error: Please enter valid numbers")

if __name__ == "__main__":
    main()