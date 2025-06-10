n = int(input("son >> "))# 12345

s = 0
while n != 0:
    s += n % 10   # s += 5
    n //= 10 # s = 1234

print(s)