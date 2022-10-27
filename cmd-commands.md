
cls            (clear screen) ekrandaki tüm yazıları temizler
xyz /?       (xyz bir komut olmak üzere) herhangi bir komut hakkında bilgi almak için kullanılır
time         geçerli zamanı saat dakika saniiye cinsinden gösterir
date         geçerli zamanı saat dakika saniiye cinsinden gösterir

dir jokerleri: soru işareti (? ) ve yıldız (*) dır.

Yıldız (*): kelimede bilinmeyen yerler için kullanılır.
Örneğin:
a*.txt şeklinde arama yapıldığında baş harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.
*a.txt şeklinde arama yapıldığında son harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.
*.txt şeklinde arama yapıldığında dosya uzantısı "txt" olan tüm dosyalar listelenir.
ahmet.*xt şeklinde arama yapıldığında adı ahmet ve dosya uzantısının sonu "xt" olan tüm dosyalar listelenir.
ahmet.tx* şeklinde arama yapıldığında adı ahmet ve dosya uzantısının başı "tx" olan tüm dosyalar listelenir.
ahmet.* şeklinde arama yapıldığında adı ahmet olan tüm dosyalar listelenir.
*.* şeklinde arama yapıldığında ise tüm dosyalar listelenir.

Soru işareti (?): kelimelerde bilinmeyen harf/sembol/sayı vs. için kullanılır. (her bir soru işareti tek karakterdir.) 
Örneğin:
ah??t şeklinde arama yapıldığında eğer dosya içerisinde "ahmet, ahhmt, ahmeet ..." dosyalarının olduğunu düşünürsek,
arama sonucu olarak bize "ahmet, ahhmt" sonuçlarını verir.

ctrl + c      komutu durdurur.
dir /p        dosyaların içini gösterir
dir /s        bulunduğu konumun içindeki dosyların alt klasörlerini gösterir

dir /o        genel sıralama
dir /od      tarihe göre sıalama
dir /oe      klasör ve dosyaların uzuntılarının alfabetik sıralamaya yarar
dir /on      klasör ve dosyaları alfabetik sıralamaya göre sıralar
dir /os      klasör ve dosyaların boyutlarına göre sıralar
dir /a        dosyaların niteliklerini gösterir (dosya gizli olabilir, dosya sistem dosyası olabilir, arşiv dosyası olabilir ...)
dir /aa      sadece arşivleri gösterir.
dir /ar       sadece okunabilir dosyalar.
dir /ah      sadece gizli dosyaları gösterir.
dir /ad      sadece dizinleri gösterir.
dir /as      sadece sistem dosyalarını gösterir.

attrib -H -R -S /S /D G:\*.*       gizli dosyaların gösterilmesini sağlar.

cd                           change directory (dizin değiştirme)
cd ..                        bir üst dosyaya çıkmak için kullanılır
cd (dosya yolu)      dosyanın bulunduğu konuma ulaşmak için kullanılır.
cd \                        ana konuma geri döndürür.

md  "dosya adı      (make directory) klasör oluştrma işlemidir.
rd  "dosya adı"      (remove directory) klasor kaldırma işlemidir.
vol
ver
prompt                  varsayılan komum
prompt $p C:\       varsayılan konuma geçer (C:\)
prompt $t             geçerli zamana geçer.
prompt $d            geçerli tarihe geçer.

iç komutlar:          bilgisarda o dosya olmasa bile çalışan komutlardır.
dış komutlar:        dosyaya bağlı çalışır.

copy con a.txt             dosya oluşturma ve içerisine yazılar yazma işlemidir
type a.txt                    dosya içeriğini görme
ren                              dosyanın adını ve soyadını değişirmeye yarar.
ren a.txt deneme.txt   dosya adını değiştirme
ren a.txt a.bat             dosya soyadını değiştirme
del a.txt                      dosyayı kaldırma
del *.txt                      soyadı txt olan tüm dosyaları silmek için kullanılır
del a.*                        adı a olan tüm dosyaları silmek için kullanılır
del *.*                        tüm dosyaları silmek için kullanılır (klasörler silinmez)

del dosya siler, rd klasör siler.

copy b.txt x.kal         b.txt dosya içeğini kopyalar ve x.kal dosyası oluşturur içeriğini b.txt ile aynı yapar.
copy *.* C:\asd         C de bulunan asd içerisine bulunulan konumdaki dosyaları kopyalar
