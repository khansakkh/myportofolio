Nama : Khansa 
Update dari branch latihan 

Tugas 2
1. Saat pengguna membuka halaman portofolio baru, alurnya adalah : request dari first browser diterima 'urls.py' pada level proyek seperti portofolio/urls.py, yang tugasnya adalah match path URL dengan pola yang ada. Karena path 'education/' diarahkan dengan 'include()' ke app main permintaan kemudian dikirim ke 'urls.py' pada level aplikasi main/urls.py, yang mencari pola URL spesifik dan memetakannya ke fungsi view yang sesuai yaitu show_education. View ini kemudian mengambil seluruh data dari model 'Education' dengan 'Education.objects.all()', memasukkannya ke dalam sebuah context dan meneruskan context nya ke template 'education_list.html' menggunakan 'render()'. Template kemudian menggunakan Django Template Language untuk melakukan perulangan ('{% for %}') terhadap data pada context, menampilkan setiap objek Education dalam bentuk HTML, sebelum akhirnya HTML tersebut dikirim kembali sebagai response dan ditampilkan oleh browser.

Data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template karena beberapa alasan utama. Pertama, memisahkan data dari tampilan membuat data menjadi terstruktur dan dapat dikelola melalui database, sehingga perubahan data tidak memerlukan perubahan kode HTML maupun proses deployment ulang. Kedua, data yang tersimpan di model dapat divalidasi, difilter, atau diurutkan dengan mudah menggunakan Django ORM sebelum ditampilkan. Kemudian hal ini juga membuat pengujian menjadi lebih mudah, karena skenario data kosong maupun data terisi dapat disimulasikan langsung melalui model tanpa perlu mengubah template. Jika data ditulis langsung di HTML, aplikasi menjadi sulit dikembangkan dan rentan terhadap duplikasi maupun inkonsistensi data di berbagai halaman.

2. makemigrations berfungsi untuk membuat file migrasi baru based on perubahan yang dilakukan pada model. Namun perintah ini belum  mengubah struktur database langsung, hanya menghasilkan rencana perubahan dalam bentuk berkas Python di folder migrations. Sementara itu, migrate berfungsi untuk menerapkan perubahan yang tercatat pada berkas migrasi tersebut ke dalam skema database yang sesungguhnya. Contoh kasus yang harus menjalankan kedua perintah tersebut adalah ketika membuat model baru Education pada tugas ini, setelah menambahkan class Education di models.py, perintah `python manage.py makemigrations` dijalankan untuk menghasilkan file migrasi baru 0002_education.py yang mendeskripsikan tabel baru tersebut, kemudian perintah `python manage.py migrate` dijalankan membuat tabel Education pada database sesuai skema yang telah didefinisikan.


Tugas 3

1.
ModelForm digunakan karena Django dapat otomatis membuat field pada form berdasarkan field yang terdapat pada model, termasuk validasi tipe data dan aturan yang telah didefinisikan seperti max_length dan required/optional. Hal ini dapat mengurangi duplikasi kode dibandingkan dengan menulis form HTML secara manual karena setiap input dan validasinya tidak perlu ditulis ulang secara terpisah.

csrf_token ditambahkan untuk melindungi aplikasi dari CSRF, yaitu ketika pihak lain mencoba mengirimkan request palsu atas nama pengguna yang sedang login tanpa sepengetahuan pengguna tersebut. Django menghasilkan token unik pada setiap form yang kemudian divalidasi di sisi server sebelum request diproses.

2
JSON lebih sering digunakan dibandingkan XML karena memiliki struktur yang lebih ringkas dan tidak memerlukan closing tag pada setiap elemen, sehingga ukuran datanya lebih kecil. Selain itu, JSON memiliki format yang mudah digunakan dengan JavaScript sehingga proses *parsing* di sisi client lebih sederhana. Sementara itu, XML memiliki struktur yang lebih kompleks dan membutuhkan parsing yang lebih berat. Oleh karena itu, JSON lebih efisien untuk digunakan dalam komunikasi API pada aplikasi web modern.

3
Ketika view mengembalikan data dalam bentuk JSON, prosesnya dimulai dengan melakukan query terhadap data model melalui ORM, misalnya Education.objects.all(). Query tersebut menghasilkan queryset yang berisi objek-objek Python berupa instance dari model Django.

Objek belum dapat langsung dikirim sebagai HTTP response karena masih berupa objek Python, bukan data dalam format yang dapat dibaca oleh client. Oleh karena itu, diperlukan serialization untuk mengubah objek model menjadi data dalam format terstruktur JSON, sehingga dapat dipahami client atau sistem lain di luar Django.

Setelah serialization selesai, data kemudian dibungkus dalam HttpResponse dengan content_type application/json. Dengan demikian, browser atau aplikasi client dapat mengetahui bahwa data yang diterima merupakan response dalam format JSON.
