import requests
print("Selamat Datang di Aplikasi Tomatos")
print("Silakan pilih Opsi: ")
print(" 1.Mencari Resto")
print(" 2.Daily Menu")
Host = 'https://developers.zomato.com/api/v2.1' #host untuk akses API
Key = '5d7b6a190680b1e7055412be09e73580' #key untuk get API
Headinfo = {"user-key": Key} # key API
loc = '/cities'
pilih = input("pilih: ") #untuk memilih opsi antara mencari resto atau melihat daily menu resto
while True: #melakukan kondisi looping, agar jika error akan melakukan running secara otomatis
    try: #memberikan kondisi try dan except, agar ketika error tidak terjadi bug
        pilih = int(pilih)
        while (pilih > 2 or pilih < 1)  : #melakukan looping jika angka yang di input tidak sesuai opsi
            print("Opsi yang anda pilih tidak ada, Silahkan pilih antara angka 1 atau 2 ")
            print("="*100)
            print("Selamat Datang di Aplikasi Tomatos")
            print("Silakan pilih Opsi: ")
            print(" 1.Mencari Resto")
            print(" 2.Daily Menu")
            pilih = int(input("pilih: "))
            #1. mencari resto
        if pilih == 1: 
            kota = input("Masukan Nama Kota: ")
            url_kota = f"{Host}{loc}?q={kota}"
            data_kota = requests.get(url_kota, headers = Headinfo)
            output = data_kota.json()
            while True : 
        #melakukan looping lagi agar jika ada error, tidak kembali ke proses awal
                try: 
                    lokasi = output['location_suggestions']
                    loc_id =(lokasi[0]['id'])
                    cari = '/search'
                    jumlah_resto = input("Masukan jumlah restoran yang akan ditampilkan: ")
                    try:
                        jumlah_resto = int(jumlah_resto)
                        while jumlah_resto <0 : #melakukan looping ketika format tidak sesuai
                            print('format yang anda tulis salah')
                            print('='*100)
                            jumlah_resto = int(input("Masukan jumlah restoran yang akan ditampilkan: "))
                        url_search = f"{Host}{cari}?entity_id={loc_id}&entity_type=city&count={jumlah_resto}" #url untuk melihat restaurant yang ada dikota tersebut
                        data_cari = requests.get(url_search, headers =Headinfo)
                        hasil = data_cari.json()
                        #melakukan looping untuk mencetak informasi detail dari restoran
                        for i  in range (jumlah_resto): 
                            print(f"{i+1}. Restaurant name: {hasil['restaurants'][i]['restaurant']['name']}")
                            print(f"   Establishment name: {hasil['restaurants'][i]['restaurant']['establishment']}")
                            print(f"   Cuisine name: {hasil['restaurants'][i]['restaurant']['cuisines']}")
                            print(f"   Address: {hasil['restaurants'][i]['restaurant']['location']['address']}")
                            print(f"   Phone number: {hasil['restaurants'][i]['restaurant']['phone_numbers']}")
                            print(f"   Rating: {hasil['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']}")
                            print(f"   Total review: {hasil['restaurants'][i]['restaurant']['all_reviews_count']}")
                        break #dilakukan break agar tidak terjadi looping ketika data resto berhasil ditampilkan
                    except:
                        print('Format harus angka')
                        print('='*100)
                except:
                    print('Nama kota tidak ada di bumi')
                    print('='*100)
                    kota = input("Masukan Nama Kota: ")
                    url_kota = f"{Host}{loc}?q={kota}"
                    data_kota = requests.get(url_kota, headers = Headinfo)
                    output = data_kota.json()
                    continue #fungsi ini agar kembali looping ke proses 1
#   untuk melihat menu harian sebuah resto
        if pilih == 2 :
            print("2. Daily Menu")
            resto = input("Masukkan Nama Resto: ")
            kota = input("Masukkan Nama Kota: ")
                #Mencari ID Nama kota yang diinput
            url_kota = f"{Host}{loc}?q={kota}" #url untuk mendapatkan ID nama kota
            
            while True : 
                try :
                    data_kota = requests.get(url_kota, headers = Headinfo)
                    output = data_kota.json()
                    lokasi = output['location_suggestions']
                    loc_id =(lokasi[0]['id'])
                    cari = '/search'
                    url_search = f"{Host}{cari}?entity_id={loc_id}&entity_type=city&q={resto}&count=1" 
                    #url untuk melihat restaurant yang ada dikota tersebut
                    data_cari = requests.get(url_search, headers =Headinfo)
                    hasil = data_cari.json()
                    resto_id =  (hasil["restaurants"][0]["restaurant"]['id'])
                    nama_resto =  (hasil["restaurants"][0]["restaurant"]["name"])
                    url_resto= f"{Host}/dailymenu?res_id={resto_id}"
                    data_resto = requests.get(url_resto, headers =Headinfo)
                    hasil_resto = data_resto.json()
                    print(f"Total menu di restoran tersebut sejumlah: {len(hasil_resto['daily_menus'][0]['daily_menu']['dishes'])} ")
                    jumlah_menu = int(input("Jumlah Menu yang akan ditampilkan: "))
                    for i  in range (jumlah_menu):
                        print(f"{i+1}.Nama Makanan {hasil_resto['daily_menus'][0]['daily_menu']['dishes'][i]['dish']['name']}")
                        print(f"  Harga Makanan    {hasil_resto['daily_menus'][0]['daily_menu']['dishes'][i]['dish']['price']}")        
                    break
                except:
                    print(f"restaurant {resto} tidak menampilkan daily menu")
                    print('='*100)
                    resto = input("Masukkan Nama Resto: ")
                    kota = input("Masukkan Nama Kota: ")
                #Mencari ID Nama kota yang diinput
                    url_kota = f"{Host}{loc}?q={kota}"
                    data_kota = requests.get(url_kota, headers = Headinfo)
                    output = data_kota.json()
                    continue
        break
    except:
        print('Format salah')
        print("="*100)
        print("Selamat Datang di Aplikasi Tomatos")
        print("Silakan pilih Opsi: ")
        print(" 1.Mencari Resto")
        print(" 2.Daily Menu")
        Host = 'https://developers.zomato.com/api/v2.1' #host untuk akses API
        Key = '5d7b6a190680b1e7055412be09e73580' #key untuk get API
        Headinfo = {"user-key": Key} # key API
        loc = '/cities'
        pilih = input("pilih: ")
        continue
#     return pilih
