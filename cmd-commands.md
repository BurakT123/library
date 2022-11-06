- `cls`: (clear screen) ekrandaki tüm yazıları temizler.
- `xyz /?`: (xyz bir komut olmak üzere) herhangi bir komut hakkında bilgi almak için kullanılır.
- `time`: Geçerli zamanı saat dakika saniiye cinsinden gösterir.
- `date`: Geçerli zamanı saat dakika saniiye cinsinden gösterir.

<br>

- dir jokerleri: soru işareti (? ) ve yıldız (*) dır.
- Yıldız (*): kelimede bilinmeyen yerler için kullanılır.
- Örneğin:
- `a*.txt` şeklinde arama yapıldığında baş harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.
- `*a.txt` şeklinde arama yapıldığında son harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.
- `*.txt` şeklinde arama yapıldığında dosya uzantısı "txt" olan tüm dosyalar listelenir.
- `ahmet.*xt` şeklinde arama yapıldığında adı ahmet ve dosya uzantısının sonu "xt" olan tüm dosyalar listelenir.
- `ahmet.tx*` şeklinde arama yapıldığında adı ahmet ve dosya uzantısının başı "tx" olan tüm dosyalar listelenir.
- `ahmet.*` şeklinde arama yapıldığında adı ahmet olan tüm dosyalar listelenir.
- `*.*` şeklinde arama yapıldığında ise tüm dosyalar listelenir.
- Soru işareti (?): kelimelerde bilinmeyen harf/sembol/sayı vs. için kullanılır. (her bir soru işareti tek karakterdir.) 
- Örneğin:
- 
`ah??t` şeklinde arama yapıldığında eğer dosya içerisinde `"ahmet, ahhmt, ahmeet ..."` dosyalarının olduğunu düşünürsek, arama sonucu olarak bize `"ahmet, ahhmt"` sonuçlarını verir.


<br>

- `ctrl + c`: Komutu durdurur.
- `dir /p`: Fosyaların içini gösterir
- `dir /s`: Bulunduğu konumun içindeki dosyların alt klasörlerini gösterir

<br>

- `dir /o`: Genel sıralama
- `dir /od`: Tarihe göre sıalama
- `dir /oe`: Klasör ve dosyaların uzuntılarının alfabetik sıralamaya yarar.
- `dir /on`: Klasör ve dosyaları alfabetik sıralamaya göre sıralar.
- `dir /os`: Klasör ve dosyaların boyutlarına göre sıralar.
- `dir /a`: Dosyaların niteliklerini gösterir (dosya gizli olabilir, dosya sistem dosyası olabilir, arşiv dosyası olabilir ...)
- `dir /aa`: Sadece arşivleri gösterir.
- `dir /ar`: Sadece okunabilir dosyalar.
- `dir /ah`: Sadece gizli dosyaları gösterir.
- `dir /ad`: Sadece dizinleri gösterir.
- `dir /as`: Sadece sistem dosyalarını gösterir.

<br>

- `attrib -H -R -S /S /D G:\*.*`: Gizli dosyaların gösterilmesini sağlar.

<br>

- `cd`: Change directory (dizin değiştirme)
- `cd ..`: Bir üst dosyaya çıkmak için kullanılır
- `cd (dosya yolu)`: Dosyanın bulunduğu konuma ulaşmak için kullanılır.
- `cd \`: Ana konuma geri döndürür.

<br>

- `md  "dosya adı`: (make directory) klasör oluştrma işlemidir.
- `rd  "dosya adı"`: (remove directory) klasor kaldırma işlemidir.
- `vol`:
- `ver`:
- `prompt`: Varsayılan komum
- `prompt $p C:\`: Varsayılan konuma geçer (C:\)
- `prompt $t`: Geçerli zamana geçer.
- `prompt $d`: Geçerli tarihe geçer.

<br>

- iç komutlar: Bilgisarda o dosya olmasa bile çalışan komutlardır.
- dış komutlar: Dosyaya bağlı çalışır.

<br>

- `copy con a.txt`: Dosya oluşturma ve içerisine yazılar yazma işlemidir
- `type a.txt`: Dosya içeriğini görme
- `ren`: Dosyanın adını ve uzantısını değişirmeye yarar.
- `ren a.txt deneme.txt`: Dosya adını değiştirme
- `ren a.txt a.bat`: Dosya uzantısını değiştirme
- `del a.txt`: Dosyayı kaldırma
- `del *.txt`: Uzantısı txt olan tüm dosyaları silmek için kullanılır
- `del a.*`: Adı a olan tüm dosyaları silmek için kullanılır
- `del *.*`: Tüm dosyaları silmek için kullanılır (klasörler silinmez)
- `del`: Dosya siler, `:rd`: Klasör siler.
- `copy b.txt x.kal`: b.txt dosya içeğini kopyalar ve x.kal dosyası oluşturur içeriğini b.txt ile aynı yapar.
- `copy *.* C:\asd`:C de bulunan asd içerisine bulunulan konumdaki dosyaları kopyalar