text = input("Matn kiriting: ")

s = 0
for i in text:
    if i in 'aeiou':
        s += 1

print(s)
