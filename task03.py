# Foydalanuvchi matn kiritadi
matn = input("Matn kiriting: ")

# Katta harflar sonini hisoblash
katta_harf_soni = 0

for belgi in matn:
    if 'A' <= belgi <= 'Z':
        katta_harf_soni += 1

# Natijani chiqarish
print("Katta harflar soni:", katta_harf_soni)
