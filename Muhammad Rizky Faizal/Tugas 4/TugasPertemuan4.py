class FileAnalyzer:
    def __init__(self, filename):
        """Inisialisasi dengan nama file."""
        self.filename = filename
        self.result_filename = filename + "_result.txt"

    def count_chars(self):
        """Menghitung jumlah karakter per baris dan menulis hasilnya ke file hasil."""
        try:
            # Membuka file untuk membaca
            with open(self.filename, 'r') as file:
                lines = file.readlines()

            # Memeriksa apakah file kosong
            if not lines:
                # Jika file kosong, menulis "NULL" ke file hasil
                self._write_to_file("NULL")
                print(f"Output berhasil ditulis pada {self.result_filename}")
                return

            # Menghitung jumlah karakter per baris dan detail perhitungan
            min_chars, max_chars, range_chars = self._analyze_chars(lines)

            # Menulis hasil perhitungan ke dalam file hasil
            result = (
                "\n###########\n"
                f"Min: {min_chars} karakter\n"
                f"Max: {max_chars} karakter\n"
                f"Range: {range_chars} karakter\n"
            )
            self._write_to_file(result)

            print(f"Output berhasil ditulis pada {self.result_filename}")

        except FileNotFoundError:
            print("File tidak ditemukan :(")
        except Exception as e:
            print(f"Terjadi kesalahan: {str(e)}")

    def _analyze_chars(self, lines):
        """Menghitung jumlah karakter minimum, maksimum, dan rentang dari sebuah daftar baris."""
        char_counts = [len(line.rstrip('\n')) for line in lines]
        min_chars = min(char_counts)
        max_chars = max(char_counts)
        range_chars = max_chars - min_chars
        return min_chars, max_chars, range_chars

    def _write_to_file(self, content):
        """Menulis konten ke file hasil (menambah atau mengganti isi file)."""
        with open(self.result_filename, 'w') as file:
            file.write(content)


# Main program
if __name__ == "__main__":
    # Meminta pengguna untuk memasukkan nama file input
    filename = input("Masukkan nama file input: ")
    
    # Membuat objek dari kelas FileAnalyzer
    analyzer = FileAnalyzer(filename)
    
    # Memanggil metode count_chars untuk menghitung karakter
    analyzer.count_chars()
