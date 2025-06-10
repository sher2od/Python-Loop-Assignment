matn = input("Matn kiriting: ")
teskari = ""

for i in range(len(matn) - 1, -1, -1):
    teskari += matn[i]

print("Teskari matn:", teskari)
