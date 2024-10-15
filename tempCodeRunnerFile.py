#nomor satu
def evaluate_performance(percentage):                          #membuat fungsi evaluate_performance dengan kata kunci def
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
percentage = int(input("Enter the student's percentage: "))  #untuk memasukkan nilai siswa
print(evaluate_performance(percentage))   