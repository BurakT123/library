for i in range(0, 10):
    print("\n\n",i+1,". TOPLAMA İŞLEMİ BAŞLADI...")
    def information(number):
        if number < 0:
            print("ℹ️ 0 > sayı")
        elif number > 0:
            print("ℹ️ 0 < sayı")
        else:
            print("ℹ️ 0 = sayı")


    print("👉 Lütfen birinci sayıyı yazınız.")
    def xxx ():
        global x
        try:
            x = int(input())
            information(x)
        except ValueError:
            print("❎ Lütfen bir sayı yazınız.")
            xxx()
    xxx ()

    print("👉 Lütfen ikinci sayıyı yazınız.")
    def yyy ():
        global y
        try:
            y = int(input())
            information(y)
        except ValueError:
            print("❎ Lütfen bir sayı yazınız.")
            yyy()
    yyy ()

    z = x + y


    print("\n\nToplama işlemi sonucu:", z)