import streamlit as st

from streamlit_option_menu import option_menu

# nafigasi sidebar
with st.sidebar:
    selected = option_menu('Home',
                          ['Halaman Utama','Pendahuluan','Kalkulator Kalori Harian',
                          'About Us'],
                          default_index = 0)

# halaman halaman utama
if (selected == 'Halaman Utama'):
    st.subheader('Hi Precious People :wave:')
    st.title('__**APLIKASI PERHITUNGAN KEBUTUHAN KALORI HARIAN**__')
    
    st.write('---')
    st.write('__**PENDAHULUAN**__- Sebuah aplikasi yang dibuat untuk menghitung kebutuhan kalori agar kebutuhan kalori pengguna terpenuhi. Idealnya, kebutuhan kalori per hari pada anak-anak biasanya berkisar antara 1.000-2.000 kalori. Sementara itu, remaja membutuhkan kalori sebanyak 2.000-2.650 kalori per hari. Pada orang dewasa, wanita membutuhkan sekitar 2.100 kalori per hari, sedangkan kebutuhan kalori per hari pria sekitar 2.500 kalori. Saat memasuki usia lanjut, aktivitas Anda cenderung berkurang. Akibatnya, kebutuhan kalori lansia menjadi lebih sedikit daripada kebutuhan kalori orang dewasa pada umumnya.')

# halaman Pendahuluan
if (selected == 'Pendahuluan'):
    st.title('Informasi Seputar Kalori')
    st.subheader('Makanan Yang Paling Banyak Mengandung Kalori')
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.write('Istilah kalori sangat sering dikait-kaitkan dengan program diet. Perlu anda tahu, sebenarnya bukan kalori yang menjadi penyebab utama kegemukan. Kalori justru sangat dibutuhkan tubuh untuk menghasilkan energi sehingga kita bisa melakukan aktifitas kita sehari-hari. Hanya saja, jika kalori yang masuk ke tubuh Anda melebihi batas kebutuhan kalori perhari, itulah yang menyebabkan Anda mengalami kegemukan. Kalori adalah satuan unit yang digunakan untuk mengukur nilai energi. Kandungan kalori dalam makanan tergantung pada kandungan karbohidrat, protein, dan lemak yang terdapat pada makanan tersebut. Lemak menghasilkan kalori paling banyak, yaitu 9 kalori / gram.')
    with right_column:
        st.write('Sedangkan karbohidrat dan protein mengandung 4 kalori setiap gramnya. Makanan yang mengandung banyak lemak adalah makanan yang mengandung tinggi kalori. Sebaliknya, makanan yang mengandung air tinggi seperti buah - buahan dan sayuran memiliki kadar kalori yang rendah. Kelebihan atau kekurangan kalori memiliki efek tersendiri. Berlebihan mengonsumsi kalori dapat meningkatkan risiko obesitas dan penyakit lain, seperti hipertensi, penyakit jantung, hingga stroke. Sementara itu, kekurangan kalori bisa membuat tubuh mudah lelah, berat badan kurang atau kurang gizi, atau dapat menyebabkan kekebalan tubuh menurun.')
    st.write('__**Berikut ini adalah daftar kalori makanan**__')
    st.write('[Clik here to view >](https://drive.google.com/file/d/1XzRBXErOgxl5ZS6aXSfUKeTB3acr_v5x/view?usp=share_link)')

# halaman kalkulator kalori harian
if (selected == 'Kalkulator Kalori Harian'):
    st.subheader('Perhitungan Kebutuhan Kalori Harian')
    st.write('Kalori yang dibutuhkan oleh tubuh per hari')
    
    # Input data
    usia = st.number_input("Masukkan usia Anda:", min_value=0, max_value=150, value=25, step=1)
    jenis_kelamin = st.selectbox("Masukkan jenis kelamin Anda:", ("Pria", "Wanita"))
    berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0, max_value=500.0, value=60.0, step=0.1)
    tinggi_badan = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=0.0, max_value=300.0, value=170.0, step=0.1)
    aktivitas_fisik = st.selectbox("Masukkan level aktivitas fisik Anda:", ("Sangat Sedikit Aktif (jarang berolahraga/tidak sama sekali)", "Sedikit Aktif (berolahraga (ringan) 1-3 hari dalam seminggu)", "Cukup Aktif (berolraga (sedang) 3-5 hari dalam seminggu)", "Sangat Aktif (berolahraga (berat) 6-7 hari dalam seminggu)", "Ekstrem Aktif (berolahraga (sangat berat) 6-7 hari dalam seminggu atau melakukan pekerjaan fisik yang ekstra)"))
    
    # Konversi tinggi badan dari cm
    tinggi_badan = tinggi_badan / 100
    
    # Hitung BMR (Basal Metabolic Rate) menggunakan rumus Harris-Benedict
    if jenis_kelamin == "Pria":
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi_badan * 100) - (5.677 * usia)
    else:
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi_badan * 100) - (4.330 * usia)
        
    # Hitung kebutuhan kalori harian dengan memperhitungkan aktivitas fisik
    if aktivitas_fisik == "Sangat Sedikit Aktif (jarang berolahraga/tidak sama sekali)":
        kebutuhan_kalori = bmr * 1.2
    elif aktivitas_fisik == "Sedikit Aktif (berolahraga (ringan) 1-3 hari dalam seminggu)":
        kebutuhan_kalori = bmr * 1.375
    elif aktivitas_fisik == "Cukup Aktif (berolraga (sedang) 3-5 hari dalam seminggu)":
        kebutuhan_kalori = bmr * 1.55
    elif aktivitas_fisik == "Sangat Aktif (berolahraga (berat) 6-7 hari dalam seminggu)":
        kebutuhan_kalori = bmr * 1.725
    else:
        kebutuhan_kalori = bmr * 1.9

    # Tampilkan hasil
    tombol = st.button('Hitung Kebutuhan Kalori Harian')
    if tombol:
        st.write("Kebutuhan kalori harian Anda adalah:", kebutuhan_kalori, "kalori per hari.")
        
# halaman about us
if (selected == 'About Us'):
    st.subheader('Kelompok 1 HHH LPK :sunglasses:')
    st.write('''Web aplikasi ini dibuat dan dikembangkan oleh kelompok 1 LPK, Kelas 1H Analisis Kimia dengan anggota kelompok:
1. Adinda Ratu Nurhaliza (2260001)
2. Charine Maulia Fadhelika (2260012)
3. Ilham Falas Nasution (2260023)
4. Nazwa Luthfiyah Yasmin (2260034)
5. Revizia Bellamy (2260045)
6. Yulia Ismayanti (2260056)
''')
              
    # penutup
    st.write('Terima Kasih telah mengunjungi halaman web aplikasi kami, semoga dapat bermanfaat:smile:')
