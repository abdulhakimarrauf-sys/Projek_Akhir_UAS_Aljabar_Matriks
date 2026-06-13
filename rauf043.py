class RAHA:
    def __init__(self, data):
        self.data = data
        self.shape = (len(data), len(data[0])) if isinstance(data, list) and isinstance(data[0], list) else (len(data),)

    def transpos(self):
        if len(self.shape) != 2:
            raise ValueError("Transpose hanya didukung untuk matriks 2 Dimensi.")
        baris, kolom = self.shape
        data_transpos = [[self.data[i][j] for i in range(baris)] for j in range(kolom)]
        return RAHA(data_transpos)

    def kali(self, matriks_lain):
        if self.shape[1] != matriks_lain.shape[0]:
            raise ValueError("Ukuran matriks tidak memenuhi syarat perkalian (Kolom A harus sama dengan Baris B).")
        baris_A, kolom_A = self.shape
        baris_B, kolom_B = matriks_lain.shape
        hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]
        for i in range(baris_A):
            for j in range(kolom_B):
                for k in range(kolom_A):
                    hasil[i][j] += self.data[i][k] * matriks_lain.data[k][j]
        return RAHA(hasil)

    def determinan_2x2(self):
        if self.shape != (2, 2):
            raise ValueError("Fungsi ini khusus untuk matriks berukuran 2x2.")
        a = self.data[0][0]
        b = self.data[0][1]
        c = self.data[1][0]
        d = self.data[1][1]
        return (a * d) - (b * c)

    def __repr__(self):
        tampilan = ""
        for baris in self.data:
            tampilan += f"{baris}\n"
        return f"{tampilan}Ukuran: {self.shape}"
