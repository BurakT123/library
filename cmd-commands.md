<p><code>cls</code>: (clear screen) ekrandaki tüm yazıları temizler.</p>
<p><code>xyz /?</code>: (xyz bir komut olmak üzere) herhangi bir komut hakkında bilgi almak için kullanılır.</p>
<p><code>time</code>: Geçerli zamanı saat dakika saniiye cinsinden gösterir.</p>
<p><code>date</code>: Geçerli zamanı saat dakika saniiye cinsinden gösterir.</p>

<br>

<p>dir jokerleri: soru işareti (? ) ve yıldız (*) dır.</p>
<p>Yıldız (*): kelimede bilinmeyen yerler için kullanılır.</p>
<p>Örneğin:</p>
<p><code>a*.txt</code> şeklinde arama yapıldığında baş harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.</p>
<p><code>*a.txt</code> şeklinde arama yapıldığında son harfi "a" ve dosya uzantısı "txt" olan tüm dosyalar listelenir.</p>
<p><code>*.txt</code> şeklinde arama yapıldığında dosya uzantısı "txt" olan tüm dosyalar listelenir.</p>
<p><code>ahmet.*xt</code> şeklinde arama yapıldığında adı ahmet ve dosya uzantısının sonu "xt" olan tüm dosyalar listelenir.</p>
<p><code>ahmet.tx*</code> şeklinde arama yapıldığında adı ahmet ve dosya uzantısının başı "tx" olan tüm dosyalar listelenir.</p>
<p><code>ahmet.*</code> şeklinde arama yapıldığında adı ahmet olan tüm dosyalar listelenir.</p>
<p><code>*.*</code> şeklinde arama yapıldığında ise tüm dosyalar listelenir.</p>
<p>Soru işareti (?): kelimelerde bilinmeyen harf/sembol/sayı vs. için kullanılır. (her bir soru işareti tek karakterdir.) </p>
<p>Örneğin:</p>
<p>
<code>ah??t</code> şeklinde arama yapıldığında eğer dosya içerisinde <code>"ahmet, ahhmt, ahmeet ..."</code> dosyalarının olduğunu düşünürsek, arama sonucu olarak bize <code>"ahmet, ahhmt"</code> sonuçlarını verir.
</p>

<br>

<p><code>ctrl + c</code>: Komutu durdurur.</p>
<p><code>dir /p</code>: Fosyaların içini gösterir</p>
<p><code>dir /s</code>: Bulunduğu konumun içindeki dosyların alt klasörlerini gösterir</p>

<br>

<p><code>dir /o</code>: Genel sıralama</p>
<p><code>dir /od</code>: Tarihe göre sıalama</p>
<p><code>dir /oe</code>: Klasör ve dosyaların uzuntılarının alfabetik sıralamaya yarar.</p>
<p><code>dir /on</code>: Klasör ve dosyaları alfabetik sıralamaya göre sıralar.</p>
<p><code>dir /os</code>: Klasör ve dosyaların boyutlarına göre sıralar.</p>
<p><code>dir /a</code>: Dosyaların niteliklerini gösterir (dosya gizli olabilir, dosya sistem dosyası olabilir, arşiv dosyası olabilir ...)</p>
<p><code>dir /aa</code>: Sadece arşivleri gösterir.</p>
<p><code>dir /ar</code>: Sadece okunabilir dosyalar.</p>
<p><code>dir /ah</code>: Sadece gizli dosyaları gösterir.</p>
<p><code>dir /ad</code>: Sadece dizinleri gösterir.</p>
<p><code>dir /as</code>: Sadece sistem dosyalarını gösterir.</p>

<br>

<p><code>attrib -H -R -S /S /D G:\*.*</code>: Gizli dosyaların gösterilmesini sağlar.</p>

<br>

<p><code>cd</code>: Change directory (dizin değiştirme)</p>
<p><code>cd ..</code>: Bir üst dosyaya çıkmak için kullanılır</p>
<p><code>cd (dosya yolu)</code>: Dosyanın bulunduğu konuma ulaşmak için kullanılır.</p>
<p><code>cd \</code>: Ana konuma geri döndürür.</p>

<br>

<p><code>md  "dosya adı</code>: (make directory) klasör oluştrma işlemidir.</p>
<p><code>rd  "dosya adı"</code>: (remove directory) klasor kaldırma işlemidir.</p>
<p><code>vol</code>:</p>
<p><code>ver</code>:</p>
<p><code>prompt</code>: Varsayılan komum</p>
<p><code>prompt $p C:\</code>: Varsayılan konuma geçer (C:\)</p>
<p><code>prompt $t</code>: Geçerli zamana geçer.</p>
<p><code>prompt $d</code>: Geçerli tarihe geçer.</p>

<br>

<p>iç komutlar: Bilgisarda o dosya olmasa bile çalışan komutlardır.</p>
<p>dış komutlar: Dosyaya bağlı çalışır.</p>

<br>

<p><code>copy con a.txt</code>: Dosya oluşturma ve içerisine yazılar yazma işlemidir</p>
<p><code>type a.txt</code>: Dosya içeriğini görme</p>
<p><code>ren</code>: Dosyanın adını ve uzantısını değişirmeye yarar.</p>
<p><code>ren a.txt deneme.txt</code>: Dosya adını değiştirme</p>
<p><code>ren a.txt a.bat</code>: Dosya uzantısını değiştirme</p>
<p><code>del a.txt</code>: Dosyayı kaldırma</p>
<p><code>del *.txt</code>: Uzantısı txt olan tüm dosyaları silmek için kullanılır</p>
<p><code>del a.*</code>: Adı a olan tüm dosyaları silmek için kullanılır</p>
<p><code>del *.*</code>: Tüm dosyaları silmek için kullanılır (klasörler silinmez)</p>
<p><code>del</code>: Dosya siler, </code>:rd</code>: Klasör siler.</p>
<p><code>copy b.txt x.kal</code>: b.txt dosya içeğini kopyalar ve x.kal dosyası oluşturur içeriğini b.txt ile aynı yapar.</p>
<p><code>copy *.* C:\asd</code>:C de bulunan asd içerisine bulunulan konumdaki dosyaları kopyalar</p>