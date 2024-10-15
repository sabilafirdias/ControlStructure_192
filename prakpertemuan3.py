#nomor satu
def evaluate_performance(percentage):       #membuat fungsi evaluate_performance dengan kata kunci def
    if percentage >= 90:
        return "Excellent performance"
    #jika nilai lebih dari atau sama dengan 90, maka akan tampil tulisan "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    #jika nilai lebih dari atau sama dengan 80, maka akan tampil tulisan "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    #jika nilai lebih dari atau sama dengan 70, maka akan tampil tulisan "Good performance"
    elif percentage >= 60:
        return "Average performance"
    #jika nilai lebih dari atau sama dengan 60, maka akan tampil tulisan "Average performance"
    else:
        return "BELAJAR WOY WKWKWKWKWKWK"
    #jika nilai kurang dari 60, maka akan tampil tulisan "BELAJAR WOY WKWKWKWKWKWK"
percentage = float(input("Enter the student's percentage: "))    #untuk memasukkan nilai siswa (dapat memasukkan angka desimal karena menggunakan tipe data float)
print(evaluate_performance(percentage))                          #menampilkan hasil

#nomor dua
def find_largest(a, b, c):       #membuat fungsi find_largest dengan kata kunci def untuk menemukan angka terbesar
    if a >= b and a >= c:
        return a
    #jika a lebih besar dari b dan c, maka a akan muncul sebagai angka terbesar
    elif b >= a and b >= c:
        return b
    #jika b lebih besar dari a dan c, maka b akan muncul sebagai angka terbesar
    else:
        return c
    #jika selain dua pilihan di atas, maka c akan muncul sebagai angka terbesar

a = float(input("Enter the first number: "))    #untuk memasukkan nilai (dapat memasukkan angka desimal karena menggunakan tipe data float)
b = float(input("Enter the second number: "))   #untuk memasukkan nilai (dapat memasukkan angka desimal karena menggunakan tipe data float)
c = float(input("Enter the third number: "))    #untuk memasukkan nilai (dapat memasukkan angka desimal karena menggunakan tipe data float)

print("The largest number is: ", find_largest(a, b, c))     #untuk mencetak hasil
    
#nomor tiga
def fibonacci(n):                                           #membuat fungsi deret fibonacci dengan kata kunci def
    fib_series = []                                         #membuat variabel list kosong untuk menyimpan deret fibonacci
    a, b = 0, 1                                             #membuat variabel sebagai inisial
    while a <= n:                                           #membuat perulangan selama a kurang dari atau sama dengan n
        fib_series.append(a)                                #menambahkan nilai a ke dalam list fib_series
        a, b = b, a + b                                     #memperbarui nilai a menjadi b, dan nilai b menjadi jumlah dari a + b
    return fib_series                                       #menampilkan list fib_series yang berisi deretan fibonacci
n = int(input("Enter the value of n: "))                    #untuk memasukkan nilai n
print("Fibonacci series up to", n, ":", fibonacci(n))       #menampilkan hasil deret fibonacci

#nomor empat
def print_odd_numbers(n):                       #membuat fungsi print_odd_numbers dengan kata kunci def untuk menampilkan angka-angka ganjil
    for i in range(1, n+1):                     #membuat pengulangan dari 1 sampai n
        if i % 2 != 0:                          #jika i dibagi 2 tidak sama dengan 0, maka i adalah angka ganjil
            print(i, end=" ")                   #mencetak angka ganjil, end=" " digunakan untuk memisahkan angka dengan spasi
n = int(input("Enter the value of n: "))        #untuk memasukkan nilai n
print("Odd numbers up to", n, ":")              #menampilkan pesan pemberitahuan bahwa angka yang akan muncul adalah angka ganjil hingga n
print_odd_numbers(n)                            #menampilkan angka-angka ganjil hingga n

#nomor lima
def print_pattern(n):                           #membuat fungsi print_pattern dengan kata kunci def untuk membuat pola
    for i in range(1, n + 1):                   #membuat pengulangan dari 1 sampai n
        print((str(i) + " ") * i)               #mencetak angka i sebagai string diikuti spasi, kemudian mencetak angka sebanyak i kali
n = int(input("Enter the value of n: "))        #untuk memasukkan nilai n
print_pattern(n)                                #menampilkan pola angka