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


AI DISCLOSURE
Saya menggunakan Claude (Anthropic) sebagai asisten selama mengerjakan Tutorial 03 serta Individual Assignment 2 dan 3. Penggunaannya meliputi:

Panduan implementasi skeleton template (base.html), form Create/Update/Delete, dan JSON data delivery untuk model Education.
Bantuan debugging untuk error seperti ImportError, DisallowedHost, serta konfigurasi ALLOWED_HOSTS dan CSRF_TRUSTED_ORIGINS saat deployment ke PWS.
Bantuan mengoreksi jawaban pertanyaan reflektif.

Kode inti (models, views, forms, dan urls) saya tulis dan modifikasi sendiri berdasarkan pemahaman dari penjelasan yang diberikan. Saya juga melakukan verifikasi manual dengan menjalankan python manage.py runserver dan menguji setiap fitur sebelum melakukan submit.

Tugas 4
AI Disclosure
Saya menggunakan ChatGPT sebagai alat bantu dalam pengerjaan tugas 4.
AI digunakan untuk:
- merapikan indentasi kode
- mencari letak kesalahan kode
- mengidentifikasi kode yang mungkin tidak sinkron, berbeda dengan maksud tugas
- mengerti maksud tugas
- menjelaskan makna tiap kode
- membantu menjelaskan alur dan menyelesaikan eror apabila salah

kode yang saya konsultasikan adalah kode yang saya tulis dan melanjutkan tutor yang kemudian di prompt untuk diperiksa dan disesuaikan

saya tetap menguji, mengimplementasi, menjalankan, dan mengecek serta konfigurasi django admin sendiri.

### Tugas 5

1. Debouncing adalah menunda eksekusi pencarian sampai pengguna berhenti mengetik selama jeda tertentu. Pada pencarian AJAX, ini mencegah satu request dikirim untuk setiap huruf, sehingga server tidak menerima permintaan berlebihan dan hasil pencarian tidak mudah tertimpa oleh respons dari query sebelumnya. Di halaman Education, pencarian memakai jeda 300 ms dan request sebelumnya dibatalkan dengan AbortController.
2. await menunggu Promise dari fetch() selesai sehingga kode berikutnya mendapat objek Response, bukan Promise yang masih berjalan. await juga dipakai saat membaca response.json(), karena parsing JSON bersifat asynchronous. Tanpa await, kode yang langsung mengakses status atau memanggil json() pada hasil fetch() akan bekerja pada Promise dan dapat gagal; alternatifnya adalah memakai .then() dengan alur yang setara.
3. XSS adalah serangan ketika input yang tidak tepercaya dijalankan sebagai JavaScript di browser pengguna. Data AJAX lebih rentan jika string dari JSON dimasukkan ke innerHTML, sebab JavaScript tidak otomatis melakukan escaping. Template Django secara default meng-escape nilai variabel yang dirender. Di Education, input teks dibersihkan dengan strip_tags di ModelForm dan nilai dari JSON ditampilkan lewat textContent, sehingga tag seperti <img onerror="..."> tidak dijalankan.

#### AI Disclosure

Saya menggunakan ChatGPT (OpenAI) sebagai alat bantu dalam pengerjaan Tugas 5.
AI digunakan untuk:

- membaca checklist tugas dan memeriksa kode Tutorial 05 serta fitur Education dari Tugas 3 dan 4;
- mengimplementasikan endpoint JSON, form AJAX, modal, pencarian debounce, toast, dan perlindungan XSS pada Education;
- menulis serta menjalankan pengujian, mengecek halaman lokal, dan membantu menjawab pertanyaan reflektif.

Strategi prompting saya adalah meminta AI mengikuti butir tugas satu per satu, mempertahankan hak akses yang sudah ada, menghindari fitur tambahan, serta membuat commit bertahap. Prompt lanjutan saya menekankan agar bagian disclosure ini mengikuti gaya README tugas sebelumnya. Perubahan yang dibantu AI meliputi main/views.py, main/forms.py, main/urls.py, templates/education_list.html, templates/components/education_form_modal.html, main/tests.py, dan bagian Tugas 5 pada README.md.

Keterbatasan AI: pengujian lokal tidak otomatis membuktikan deployment PWS akan berjalan identik. Karena itu, hasil di server dan tautan commit yang dikumpulkan perlu diperiksa setelah push.

#### Setup lokal

1. Buat dan aktifkan virtual environment Python.
2. Jalankan pip install -r requirements.txt.
3. Jalankan python manage.py migrate.
4. Jalankan python manage.py runserver, lalu buka /education/.

### Tugas 6

1. REST adalah gaya arsitektur yang memperlakukan data seperti Education sebagai resource dengan URL sendiri. Dalam HTTP, `GET` membaca resource, `POST` membuatnya pada endpoint daftar, dan `DELETE` menghapusnya pada endpoint detail. Setiap request membawa konteks yang dibutuhkan untuk diproses. JSON hanya menentukan format data. API yang mengembalikan JSON masih bisa mengabaikan arti method dan status HTTP. Gunakan `PUT /api/v1/education/1/` ketika mengirim representasi lengkap dari data yang bisa diedit. Gunakan `PATCH` ke URL yang sama dengan `{"end_year": 2026}` ketika hanya tahun selesai yang berubah.
2. `EducationSerializer` menentukan field API, mengubah objek `Education` menjadi data yang bisa dirender sebagai JSON, serta memvalidasi dan membersihkan input sebelum disimpan. DRF menghasilkan error per field ketika input tidak valid. Field seperti `star_count` dan `is_starred` dihitung dari relasi star dan bersifat read-only. Dengan `JsonResponse`, pemetaan field, validasi, dan bentuk respons error harus diatur secara terpisah.
3. Autentikasi menentukan identitas pengguna dari sesi login. Otorisasi menentukan apakah pengguna itu boleh melakukan suatu tindakan. Di Education, pengguna biasa bisa memberi star, Editor bisa mengubah data, dan superuser juga bisa membuat serta menghapus data. Tombol yang disembunyikan hanya mengatur tampilan. Pengguna masih bisa mengirim `POST`, `PATCH`, atau `DELETE` secara langsung, sehingga permission class harus memeriksa hak akses di server.
4. Browser bisa menyertakan cookie sesi secara otomatis. Pada request yang mengubah data, `SessionAuthentication` memeriksa token CSRF untuk mencegah situs lain memakai sesi pengguna secara tidak sah. `fetch()` mengirim token lewat `X-CSRFToken`. `force_authenticate()` menyuntikkan identitas langsung sehingga alur autentikasi sesi dilewati. Tes memakai `APIClient(enforce_csrf_checks=True)` dan `.login()` untuk membuktikan bahwa request tanpa token ditolak dan aksi star dengan token yang diterbitkan halaman Education diterima.

#### Setup dan verifikasi

1. Aktifkan virtual environment, lalu jalankan `python -m pip install -r requirements.txt` dan `python manage.py migrate`.
2. Jalankan `python manage.py test main` untuk menguji Education dan Projects.
3. Jalankan `python manage.py runserver`, lalu buka `/education/`, `/projects/`, dan `/api/v1/education/`. Endpoint terakhir menampilkan Browsable API ketika dibuka dari browser.

#### AI Disclosure

ChatGPT (OpenAI) digunakan untuk mencocokkan perubahan DRF lokal dengan checklist Tugas 6, meninjau serializer, permission, API, dan integrasi `fetch()`, memperkuat pengujian Education di `main/tests_api.py`, serta menyusun jawaban reflektif dan petunjuk verifikasi ini.

Prompt meminta ChatGPT mengikuti panduan tugas di perangkat lokal dan menggunakan commit bertahap. Dalam peninjauan, ChatGPT membandingkan aturan peran dengan tes yang sudah ada. Tes penolakan diperkuat dengan pemeriksaan jumlah dan isi data. Tes sesi login ditambahkan untuk memeriksa token pada akun biasa dan Editor. Tes Django memverifikasi respons server dan efeknya pada database. Interaksi JavaScript di browser dan deployment perlu diverifikasi terpisah.
