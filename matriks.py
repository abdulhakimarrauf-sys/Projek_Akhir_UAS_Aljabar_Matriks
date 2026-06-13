import percobaan as pn

if __name__ == "__main__":
    print("=== UJI COBA MODUL MATRIKS ===\n")

    A = pn.RAHA([[1, 2], 
                [3, 4]])
    B = pn.RAHA([[5, 6], 
                [7, 8]])
    print("Matriks A:")
    print(A)
    print("\n")
    print("Matriks B:")
    print(B)

    print("\n")

    print("1. Hasil Transpos Matriks A:")
    A_T = A.transpos()
    print(A_T)

    print("\n")

    print("2. Hasil Perkalian Matriks (A x B):")
    Hasil_Kali = A.kali(B)
    print(Hasil_Kali)

    print("\n")

    print("3. Hasil Determinan Matriks A (2x2):")
    det_A = A.determinan_2x2()
    print(f"Nilai Determinan = {det_A}")
