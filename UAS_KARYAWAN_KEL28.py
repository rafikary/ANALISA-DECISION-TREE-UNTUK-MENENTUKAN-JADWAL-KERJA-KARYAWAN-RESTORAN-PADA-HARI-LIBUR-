import numpy as np

# Data untuk kasus studi, mengandung nilai total dan atribut HLB, HLN, dan Disiplin
data = {
    'Total': {'Atur Jadwal': 8, 'Tenaga Tambahan': 9},
    'HLB': {'Kerja 1 Shift': {'Atur Jadwal': 2, 'Tenaga Tambahan': 0},
            'Kerja 2 Shift': {'Atur Jadwal': 6, 'Tenaga Tambahan': 9}},
    'HLN': {'Kerja 1 Shift': {'Atur Jadwal': 7, 'Tenaga Tambahan': 2},
            'Kerja 2 Shift': {'Atur Jadwal': 1, 'Tenaga Tambahan': 7}},
    'Disiplin': {'Baik': {'Atur Jadwal': 0, 'Tenaga Tambahan': 8},
                 'Cukup Baik': {'Atur Jadwal': 4, 'Tenaga Tambahan': 1},
                 'Kurang Baik': {'Atur Jadwal': 3, 'Tenaga Tambahan': 0}}
}

# Fungsi untuk menghitung entropi dari dua nilai
def entropy(s1, s2):
    total = s1 + s2
    if total == 0:
        return 0
    p1 = s1 / total
    p2 = s2 / total
    if p1 == 0 or p2 == 0:
        return 0
    return - (p1 * np.log2(p1) + p2 * np.log2(p2))

# Menghitung entropi total dari dataset
total_entropy = entropy(data['Total']['Atur Jadwal'], data['Total']['Tenaga Tambahan'])

# Fungsi untuk menghitung gain dari suatu atribut
def calculate_gain(attribute_data, total_entropy, total_instances):
    subsets_entropy = 0
    for subset in attribute_data.values():
        subset_total = sum(subset.values())
        subset_entropy = entropy(subset['Atur Jadwal'], subset['Tenaga Tambahan'])
        subsets_entropy += (subset_total / total_instances) * subset_entropy
    return total_entropy - subsets_entropy

# Menghitung total jumlah instance
total_instances = sum(data['Total'].values())

# Menghitung gain untuk setiap atribut
gain_hlb = calculate_gain(data['HLB'], total_entropy, total_instances)
gain_hln = calculate_gain(data['HLN'], total_entropy, total_instances)
gain_disiplin = calculate_gain(data['Disiplin'], total_entropy, total_instances)

# Fungsi untuk memprediksi hasil berdasarkan aturan pohon keputusan
def predict(discipline, hlb, hln):
    if discipline == "Baik":
        return "Tenaga Tambahan"
    elif discipline == "Cukup Baik":
        if hln == "Ya":
            return "Tenaga Tambahan"
        else:
            return "Atur Jadwal"
    elif discipline == "Kurang Baik":
        return "Atur Jadwal"
    return "Atur Jadwal"  # Kasus default

# Fungsi untuk menentukan disiplin berdasarkan HLB dan HLN
def determine_discipline(hlb, hln):
    if hlb == "1 Shift" and hln == "Tidak":
        return "Cukup Baik"
    elif hlb == "2 Shift" and hln == "Ya":
        return "Baik"
    elif hlb == "1 Shift" and hln == "Ya":
        return "Cukup Baik"
    else:
        return "Kurang Baik"

# Fungsi untuk menerima input pengguna
def input_data():
    name = input("Masukkan jenis karyawan: ")
    hlb = input("Masukkan HLB (1 Shift/2 Shift): ")
    hln = input("Masukkan HLN (Ya/Tidak): ")
    
    discipline = determine_discipline(hlb, hln)
    prediction = predict(discipline, hlb, hln)
    
    print(f"{name} dengan HLB: {hlb}, HLN: {hln} -> Disiplin: {discipline} -> Prediksi: {prediction}")
    
    return name, discipline

# Daftar untuk menyimpan karyawan terbaik
best_staff = []

# Loop untuk menerima input pengguna dan menampilkan hasil prediksi
while True:
    name, discipline = input_data()
    
    # Jika disiplin adalah "Baik", tambahkan ke daftar best staff
    if discipline == "Baik":
        best_staff.append(name)
    
    # Tanyakan apakah pengguna ingin memasukkan data lagi
    again = input("Apakah Anda ingin memasukkan data karyawan lain? (Ya/Tidak): ")
    if again.lower() != "ya":
        break

# Output the best staff
if best_staff:
    print("\nBEST STAFF:")
    for staff in best_staff:
        print(f"{staff} - BEST STAFF")
else:
    print("\nTidak ada karyawan dengan disiplin 'Baik'.")
