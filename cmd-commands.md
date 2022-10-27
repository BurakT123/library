<p>`cls`: (clear screen) ekrandaki tüm yazıları temizler.</p>
<p>`xyz /?`       (xyz bir komut olmak üzere) herhangi bir komut hakkında bilgi almak için kullanılır</p>
<p>`time`         geçerli zamanı saat dakika saniiye cinsinden gösterir</p>
<p>`date`         geçerli zamanı saat dakika saniiye cinsinden gösterir</p>

<br>

<p>dir jokerleri: soru işareti (? ) ve yıldız (*) dır.</p>
<p>Yıldız (*): kelimede bilinmeyen yerler için kullanılır.</p>
<p>Örneğin:</p>
<p>a*.txt şeklinde arama yapıldığında baş harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.</p>
<p>*a.txt şeklinde arama yapıldığında son harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.</p>
<p>*.txt şeklinde arama yapıldığında dosya uzantısı "txt" olan tüm dosyalar listelenir.</p>
<p>ahmet.*xt şeklinde arama yapıldığında adı ahmet ve dosya uzantısının sonu "xt" olan tüm dosyalar listelenir.</p>
<p>ahmet.tx* şeklinde arama yapıldığında adı ahmet ve dosya uzantısının başı "tx" olan tüm dosyalar listelenir.</p>
<p>ahmet.* şeklinde arama yapıldığında adı ahmet olan tüm dosyalar listelenir.</p>
<p>*.* şeklinde arama yapıldığında ise tüm dosyalar listelenir.</p>
<p>Soru işareti (?): kelimelerde bilinmeyen harf/sembol/sayı vs. için kullanılır. (her bir soru işareti tek karakterdir.) </p>
<p>Örneğin:</p>
<p>
ah??t şeklinde arama yapıldığında eğer dosya içerisinde "ahmet, ahhmt, ahmeet ..." dosyalarının olduğunu düşünürsek, arama sonucu olarak bize "ahmet, ahhmt" sonuçlarını verir.
</p>

<br>

<p>`ctrl + c` komutu durdurur.</p>
<p>`dir /p`       dosyaların içini gösterir</p>
<p>`dir /s`        bulunduğu konumun içindeki dosyların alt klasörlerini gösterir</p>

<br>

<p>`dir /o`        genel sıralama</p>
<p>`dir /od`      tarihe göre sıalama</p>
<p>`dir /oe`      klasör ve dosyaların uzuntılarının alfabetik sıralamaya yarar</p>
<p>`dir /on`      klasör ve dosyaları alfabetik sıralamaya göre sıralar</p>
<p>`dir /os`      klasör ve dosyaların boyutlarına göre sıralar</p>
<p>`dir /a`        dosyaların niteliklerini gösterir (dosya gizli olabilir, dosya sistem dosyası olabilir, arşiv dosyası olabilir ...)</p>
<p>`dir /aa`      sadece arşivleri gösterir.</p>
<p>`dir /ar`       sadece okunabilir dosyalar.</p>
<p>`dir /ah`      sadece gizli dosyaları gösterir.</p>
<p>`dir /ad`      sadece dizinleri gösterir.</p>
<p>`dir /as`      sadece sistem dosyalarını gösterir.</p>

<br>

<p>`attrib -H -R -S /S /D G:\*.*`       gizli dosyaların gösterilmesini sağlar.</p>

<br>

<p>`cd`                           change directory (dizin değiştirme)</p>
<p>`cd ..`                        bir üst dosyaya çıkmak için kullanılır</p>
<p>`cd (dosya yolu)`      dosyanın bulunduğu konuma ulaşmak için kullanılır.</p>
<p>`cd \`                        ana konuma geri döndürür.</p>

<br>

<p>`md  "dosya adı`      (make directory) klasör oluştrma işlemidir.</p>
<p>`rd  "dosya adı"`      (remove directory) klasor kaldırma işlemidir.</p>
<p>`vol`</p>
<p>`ver`</p>
<p>`prompt`                  varsayılan komum</p>
<p>`prompt $p C:\`       varsayılan konuma geçer (C:\)</p>
<p>`prompt $t`             geçerli zamana geçer.</p>
<p>`prompt $d`            geçerli tarihe geçer.</p>

<br>

<p>iç komutlar:          bilgisarda o dosya olmasa bile çalışan komutlardır.</p>
<p>dış komutlar:        dosyaya bağlı çalışır.</p>

<br>

<p>`copy con a.txt`             dosya oluşturma ve içerisine yazılar yazma işlemidir</p>
<p>`type a.txt`                    dosya içeriğini görme</p>
<p>`ren`                              dosyanın adını ve soyadını değişirmeye yarar.</p>
<p>`ren a.txt deneme.txt`  dosya adını değiştirme</p>
<p>`ren a.txt a.bat`         dosya soyadını değiştirme</p>
<p>`del a.txt`                  dosyayı kaldırma</p>
<p>`del *.txt`                  soyadı txt olan tüm dosyaları silmek için kullanılır</p>
<p>`del a.*`                       adı a olan tüm dosyaları silmek için kullanılır</p>
<p>`del *.*`                     tüm dosyaları silmek için kullanılır (klasörler silinmez)</p>
<p>`del` dosya siler, `rd` klasör siler.</p>
<p>`copy b.txt x.kal`         b.txt dosya içeğini kopyalar ve x.kal dosyası oluşturur içeriğini b.txt ile aynı yapar.</p>
<p>`copy *.* C:\asd`         C de bulunan asd içerisine bulunulan konumdaki dosyaları kopyalar</p>