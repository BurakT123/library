file = open("e:\ctk2.txt", "a")

title = input("Başlığı yazınız")
file.write(title + "\n\n")

file.write("-------------------------------------- \n")

for i in range(1, 5):
    name = input("Adı: ")
    surname = input("Soyadı: ")
    age = input("Yaşı: ")
    file.write(str(i) + ". " + " " + name + " " + surname + " " +  age + "\n\n")
    
file.write("--------------------------------------")

file.close()