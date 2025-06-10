import random

pin = random.randint(1000, 9999)
urinish = 0
topdi = False

print("4 xonali PIN kodni topishga harakat qiling. Sizda 7 ta urinish bor.")

while urinish < 7:
    taxmin = int(input(f"{urinish + 1}-urinish: "))
    urinish += 1

    if taxmin > pin:
        print("Juda katta son!")
    elif taxmin < pin:
        print("Juda kichik son!")
    else:
        print("Tabriklaymiz, topdingiz!")
        topdi = True
        break

if not topdi:
    print("Afsus, siz 7 marta urinib topa olmadingiz.")
    print("To'g'ri javob:", pin)
