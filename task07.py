son = int(input("1 - son > "))
eng_katta = son  # Dastlabki sonni eng katta deb olamiz

for i in range(4):  
    yangi_son = int(input(f"{i + 2} - son > "))
    if yangi_son > eng_katta:
        eng_katta = yangi_son

print("Eng katta son:", eng_katta)
