#1
print("Hello World")

#2
nama = input()
print("Hello", nama, "!")

#3
name = input()
if (name == "Alice" or name == "Bob"):
    print("Hello", name, "!")
else:
    print("Hello !")

#4
n = int(input())
x = 0
for i in range(1, n+1):
    x = x + i
print(x)

#5
n = int(input())
y = 0
for i in range(1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        y = y+i
        print(i, end=" ")
print()        
print(y)

#6
n = int(input())
total = 0
w = input("Sum or Product : ")
if w == "Sum":
    for i in range(1, n+1):
        total += i
    print(total)
else:
    for j in range(1,n+1):
        print(j)

#7
n = int(input("Perkalian : "))
for i in range(1, 13):
    print(n, "x", i, "=", n*i)
    
#8
batas = int(input("Masukkan Batas Bilangan : "))
for i in range(2, batas+1):
    m = 0
    for j in range(2, i//2+1):
        if (i % j ==0):
            m = m+1
    if m<=0:
        print(i)

#9
import random
tebak = 1
nomor = random.randint(1, 100)
tebak_list = []
n = int(input("Masukkan Nomor Tebakan : "))
while n != nomor:
    tebak_list.append(n)
    if n < nomor:
        print("Too Small")
        n = int(input("Tebak Lagi : "))
        if n == nomor:
            tebak_list.append(n)
            break
    elif n > nomor:
        print("Too Large")
        n = int(input("Tebak Lagi : "))
        if n == nomor:
            tebak_list.append(n)
            break
    elif n == nomor:
        tebak_list.append(n)
        break
        
print(tebak_list)
if n == nomor:
    for i in range (len(tebak_list)-1):
        if tebak_list[i] == tebak_list[i+1]:
            tebak += 0
        elif tebak_list[i] != tebak_list[i+1]:
            tebak += 1
print("Kamu Benar dengan Tebakan Sebanyak", tebak, "Kali")
