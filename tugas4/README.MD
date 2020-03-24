 FORMAT DARI PROTOCOL
    
    Command nya adalah 2 string yang terpisah oleh spasi
    Format : command *spasi* parameter (untuk add ada tambahan *spasi* parameter2)
    FITUR YANG BISA DILAKUKAN :
    a. Meletakkan File
       Fitur ini digunakan untuk meletakkan file ke dalam folder "dropbox"
       Request : add
       Parameter : namafile *spasi* isi dari file 
       Response yang diberikan: Jika berhasil -> "File successfully added!"
                                Jika gagal -> "ERROR"
                                
    b. List File
       Fitur ini digunakan untuk melihat list file di dalam folder 'dropbox'
       Request : list
       Parameter: -
       Response: Jika berhasil -> "List of File accepted!"
       
    c. Mengambil File
       Fitur ini digunakan untuk mengambil file berdasarkan nama file dari folder 'dropbox'
       Request : get
       Parameter : namafile yang ingin diambil
       Response: jika berhasil -> "File has been received"
                 jika gagal -> "ERROR"
    d. Jika command tidak dikenali akan merespon dengan ERRCMD
    
    
<h1> Urutan Menjalankan File </h1>
Jadi file pertama yang harus dijalankan adalah server.py. Dari server.py ini, request akan diteruskan ke file person_machine.py. 
Di person_machine.py, request akan dipecah menjadi beberapa command yang selanjutnya akan diteruskan ke file handler.py untuk dieksekusi.
Setelah di eksekusi, hasil request itu akan dikirim ke person_machine.py dan dikirim lagi ke server.py untuk ditampilkan ke user.
<img src="/tugas4/dokumentasi/server.jpg"> </img>

Setelah server dijalankan, maka salah satu dari 3 client dapat dijalankan

<ul> 
  <li> Add File </li>
  Ini ketika file tambahFile dijalankan 
  <br>
  <img src="/tugas4/dokumentasi/addFile.jpg"> </img>
  <br>
  Jika sudah dijalankan, maka file tersebut akan muncul di folder dropbox
  <br>
  <img src="/tugas4/dokumentasi/hasiladdFile.jpg"> </img>
  
  <li> Get File </li>
  Ini ketika file ambilFile dijalankan
  <br>
  <img src="/tugas4/dokumentasi/getFile.jpg"> </img>
  <br>
  Jika sudah dijalankan, maka client akan mendapatkan file tersebut di folder root
  <br>
  <img src="/tugas4/dokumentasi/hasilgetFile.jpg"> </img>
  
  <li> List File </li>
  Ini ketika file ambilListFile dijalankan, maka client akan mendapatkan list file dalam folder dropbox
  <br>
  <img src="/tugas4/dokumentasi/listFile.jpg"> </img>

</ul>

<h2>Cara Melakukan Request</h2>
Untuk cara melakukan request sebagai client, saya tidak menggunakan fungsi input().
Jadi kalau ingin mengganti file yang ingin di request, bisa diubah secara manual nama filenya di file client (kecuali fitur list karena tidak memerlukan nama file).
