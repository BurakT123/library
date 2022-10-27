
`cls`            (clear screen) ekrandaki tüm yazıları temizler
<br>
`xyz /?`       (xyz bir komut olmak üzere) herhangi bir komut hakkında bilgi almak için kullanılır
<br>
`time`         geçerli zamanı saat dakika saniiye cinsinden gösterir
<br>
`date`         geçerli zamanı saat dakika saniiye cinsinden gösterir
<br>
<br>
dir jokerleri: soru işareti (? ) ve yıldız (*) dır.
<br>
Yıldız (*): kelimede bilinmeyen yerler için kullanılır.
<br>
Örneğin:
<br>
a*.txt şeklinde arama yapıldığında baş harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.
<br>
*a.txt şeklinde arama yapıldığında son harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.
<br>
*.txt şeklinde arama yapıldığında dosya uzantısı "txt" olan tüm dosyalar listelenir.
<br>
ahmet.*xt şeklinde arama yapıldığında adı ahmet ve dosya uzantısının sonu "xt" olan tüm dosyalar listelenir.
<br>
ahmet.tx* şeklinde arama yapıldığında adı ahmet ve dosya uzantısının başı "tx" olan tüm dosyalar listelenir.
<br>
ahmet.* şeklinde arama yapıldığında adı ahmet olan tüm dosyalar listelenir.
<br>
*.* şeklinde arama yapıldığında ise tüm dosyalar listelenir.
<br>

<br>
Soru işareti (?): kelimelerde bilinmeyen harf/sembol/sayı vs. için kullanılır. (her bir soru işareti tek karakterdir.) 
<br>
Örneğin:
<br>
ah??t şeklinde arama yapıldığında eğer dosya içerisinde "ahmet, ahhmt, ahmeet ..." dosyalarının olduğunu düşünürsek,
<br>
arama sonucu olarak bize "ahmet, ahhmt" sonuçlarını verir.
<br>

`ctrl + c`      komutu durdurur.
<br>
`dir /p`       dosyaların içini gösterir
<br>
`dir /s`        bulunduğu konumun içindeki dosyların alt klasörlerini gösterir
<br>

<br>
`dir /o`        genel sıralama
<br>
`dir /od`      tarihe göre sıalama
<br>
`dir /oe`      klasör ve dosyaların uzuntılarının alfabetik sıralamaya yarar
<br>
`dir /on`      klasör ve dosyaları alfabetik sıralamaya göre sıralar
<br>
`dir /os`      klasör ve dosyaların boyutlarına göre sıralar
<br>
`dir /a`        dosyaların niteliklerini gösterir (dosya gizli olabilir, dosya sistem dosyası olabilir, arşiv dosyası olabilir ...)
<br>
`dir /aa`      sadece arşivleri gösterir.
<br>
`dir /ar`       sadece okunabilir dosyalar.
<br>
`dir /ah`      sadece gizli dosyaları gösterir.
<br>
`dir /ad`      sadece dizinleri gösterir.
<br>
`dir /as`      sadece sistem dosyalarını gösterir.
<br>

<br>
`attrib -H -R -S /S /D G:\*.*`       gizli dosyaların gösterilmesini sağlar.
<br>

<br>
`cd`                           change directory (dizin değiştirme)
<br>
`cd ..`                        bir üst dosyaya çıkmak için kullanılır
<br>
`cd (dosya yolu)`      dosyanın bulunduğu konuma ulaşmak için kullanılır.
<br>
`cd \`                        ana konuma geri döndürür.
<br>

<br>
`md  "dosya adı`      (make directory) klasör oluştrma işlemidir.
<br>
`rd  "dosya adı"`      (remove directory) klasor kaldırma işlemidir.
<br>
`vol`
<br>
`ver`
<br>
`prompt`                  varsayılan komum
<br>
`prompt $p C:\`       varsayılan konuma geçer (C:\)
<br>
`prompt $t`             geçerli zamana geçer.
<br>
`prompt $d`            geçerli tarihe geçer.
<br>

<br>
iç komutlar:          bilgisarda o dosya olmasa bile çalışan komutlardır.
<br>
dış komutlar:        dosyaya bağlı çalışır.
<br>

<br>
`copy con a.txt`             dosya oluşturma ve içerisine yazılar yazma işlemidir
<br>
`type a.txt`                    dosya içeriğini görme
<br>
`ren`                              dosyanın adını ve soyadını değişirmeye yarar.
<br>
`ren a.txt deneme.txt`  dosya adını değiştirme
<br>
`ren a.txt a.bat`         dosya soyadını değiştirme
<br>
`del a.txt`                  dosyayı kaldırma
<br>
`del *.txt`                  soyadı txt olan tüm dosyaları silmek için kullanılır
<br>
`del a.*`                       adı a olan tüm dosyaları silmek için kullanılır
<br>
`del *.*`                     tüm dosyaları silmek için kullanılır (klasörler silinmez)

`del` dosya siler, `rd` klasör siler.

`copy b.txt x.kal`         b.txt dosya içeğini kopyalar ve x.kal dosyası oluşturur içeriğini b.txt ile aynı yapar.
`copy *.* C:\asd`         C de bulunan asd içerisine bulunulan konumdaki dosyaları kopyalar
