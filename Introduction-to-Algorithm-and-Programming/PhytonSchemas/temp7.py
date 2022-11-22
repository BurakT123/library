x = int(input("Lütfen 1. dersi yazınız. \n"))
y = int(input("Lütfen 2. dersi yazınız. \n"))
z = int(input("Lütfen 3. dersi yazınız. \n"))

ort = int((x + y + z) / 3)
if ort < 50:
    durum = "Kaldı"
elif ort == 50:
    durum = "50 ile geçti..."
else:
    durum = "Geçti"

print("Durum:", durum)
print("Ortalaması:", ort)