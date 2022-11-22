def writeA ():
    global a
    a = int(input("Lütfen a sayısını yazınız. \n"))

def writeB ():
    global b
    b = int(input("Lütfen b sayısını yazınız. \n"))
    if a == b:
        print("Lütfen sayıları aynı yazmayınız!")
        writeB()

writeA()
writeB()

toplam = 0
for i in range(a, b, -1):
    toplam= i+toplam

print(toplam)