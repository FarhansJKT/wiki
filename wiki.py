import os
import sys
import time
os.system("clear")

key = "[['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
keys = f"extra-keys = {key}"
menu = "\33[31;1m█████████████████  \33[36;1mAUTHOR\33[37;1m  :\33[36;1m FHANS DZ\n\33[31;1m█████████████████  \33[36;1mGITHUB\33[37;1m  :\33[36;1m RIRIPII\n\33[37;1m█████████████████\n\33[37;1m█████████████████ \33[36;1m [\33[37;1m TERMUX INDONESIA\33[36;1m ]\n\n\33[37;1m᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁"
menu2 = "[1] UPDATE\n[2] OPEN WIKI\n[3] MENANBAHKAN EXSTRA KEY\n[4] SC LOGIN SIMPLE\n[5] CONTACK AUTHOR\n[0] EXIT TOOLS"
garis = "᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁᠁"
lengkap = "Apa itu Perintah Termux?\nPerintah termux adalah kode dalam bentuk tulisan/text yang harus kamu ketikan ke terminal termux sebagai cara untuk berinteraksi dengan shell linux android mu.\n\nInteraksi ini bisa berupa menginstall,hapus aplikasi atau membuka,memindah,menghapus,mengedit file.\n\nPerintah Termux Case Sensitive\nYang perlu kamu ketahui adalah perintah termux bersifat case sensitif dimana huruf besar dan kecil dianggap berbeda, saat kamu ingin membersihkan layar termux maka kamu harus menulis dengan tepat kode perintah clear (huruf kecil semua).\n\nJika kamu menulis Clear,cLear,…,cleaR maka perintah tersebut tidak akan dikenali karena dianggap berbeda dengan perintah yang kamu maksud “clear” huruf kecil semua.\n\nPerintah Termux dan Linux Sama\nTermux pada dasarnya terminal emulator yang digunakan untuk mengakses shell linux di android mu,jadi perintah termux sama persis dengan perintah linux,jika kamu bisa perintah linux maka kamu dengan mudah menguasai termux.\n\nUntuk memulai belajar termux minimal kamu harus tau dan hafal perintah dasar linux,jangan hanya cuma mengetik perintah yang ada di tutorial tanpa tau maksud dan fungsi dari perintah tersebut.\n\nAuto Complete di Perintah Termux\nAuto complete adalah fitur pada termux yang akan memprediksi dan menampilkan kode perintah termux yang sesuai dengan keyword yang kamu ketik, caranya yaitu cukup ketikan beberapa huruf lalu tekan tombol TAB.\n\nDengan begini kamu tidak harus 100% menghafal opsi pada perintah  linux karena hanya dengan mengetikan beberapa huruf dan menekan tombol TAB termux akan memunculkan opsi perintah yang ada.\n\nmenggunakan perintah termux\nContoh: Saat saya mengetikan apt lalu saya tekan  tombol TAB pada keyboard 2x maka akan muncul daftar perintah yang didahului dengan apt dan saat saya memilih apt-get dan kembali menekan tombol TAB 2x maka akan muncul juga pilihan/opsi yang tersedia setelah perintah apt-get.\n\nTidak berhenti sampai disini auto complete bisa terus kamu gunakan hingga saat pemilihan item atau file untuk dimasukan pada parameter perintah linux.\n\nContoh Penggunaan Kode Perintah Termux\nTermux hanya bisa digunakan dengan mengetikan kode perintah termux,hamu harus menghafalkan semua mulai dari kode perintah untuk update,install,hapus aplikasi hingga kode perintah untuk mengelola file dan folder.\n\nKode Perintah Cari,Install,Hapus,Update Aplikasi Termux\nBerbeda dengan windows,keluarga linux menyediakan semua aplikasi dalam satu server yang disebut dengan software repository.\n\nKamu bisa mencari download dan install aplikasi termux yang kamu mau dari server software repository termux dengan sangat mudah yaitu dengan menggunakan kode perintah $ pkg\n\nAplikasi pada Termux disebut juga dengan istilah Package\n\nMENAMPILKAN MENU BANTUAN\nKetikan $ pkg help untuk melihat opsi yang disediakan TERMUX pkg package manager\n\nmenampilkan opsi pkg package manager di termux\nopsi pkg package manager di TERMUX\nMENCARI APLIKASI TERMUX\nGunakan perintah $ pkg search xxxx untuk Mencari aplikasi termux berdasar nama.\n\ncara mencari aplikasi di termux\nmencari apllikasi di termux\nMENGINSTALL PACKAGES APLIKASI TERMUX\nGunakan perintah $ pkg install xxxx untuk menginstall packages aplikasi termux.\n\ncara menginstall aplikasi di termux\nmenginstall aplikasi di termux menggunakan pkg\nMENGHAPUS PACKAGES APLIKASI TERMUX\nGunakan perintah $ pkg uninstall xxxx untuk menghapus packages.\n\ncara menguninstall aplikasi di termux\nmenghapus/menguninstall aplikasi di termux\nREINSTALL PACKAGES APLIKASI TERMUX\nGunakan perintah $ pkg reinstall xxxx untuk mereinstall packages\n\ncara melakukan reinstall di termux menggunakan pkg\ncara reinstall aplikasi di termux\nINFORMASI PACKAGES APLIKASI TERMUX\nGunakan perintah $ pkg show xxxx untuk menampilkan informasi detail tentang packages.\n\ncara menampilkan informasi package aplikasi di termux\nmenampilkan informasi aplikasi di termux\nMENAMPILKAN PACKAGES APLIKASI TERMUX TERINSTALL\nGunakan perintah $ pkg list-installed untuk menampilkan daftar packages yang terinstall di termux mu.\n\nperintah untuk menampilkan aplikasi yang telah terinstall di termux\nmenampilkan aplikasi terinstall di termux\nMELIHAT LOKASI FILES PACKAGES DIINSTALL\nGunakan perintah $ pkg files xxxx untuk melihat lokasi files packages diinstall\n\nperintah untuk mengetahui lokasi file disimpan saat aplikasi diinstall\nmelihat lokasi penginstallan aplikasi di termux\nMENAMPILKAN SEMUA PACKAGES YANG TERSEDIA\nGunakan perintah $ pkg list-all untuk menampilkan semua package yang disediakan di repositori.\n\nperintah untuk menampilkan semua aplikasi yang tersedia di software repository termux\nmenampilkan semua aplikasi yang tersedia\nUPDATE dan UPGRADE PACKAGES YANG TERINSTALL\nGunakan perintah $ pkg upgrade untuk mengupdate dan upgrade package yang terinstall di termux mu\n\nperintah untuk mengupdate aplikasi yang terinstall di termux\nupdate dan upgrade aplikasi termux\nKode Perintah Mengelola file dan folder Termux\nBerikut adalah perintah dasar yang wajib kamu kuasai saat belajar menggunakan termux,perintah ini sangat berguna karena perintah termux ini sering digunakan untuk mengelola file dan folder,jika kamu serius belajar hacking kamu harus membiasakan menggunakan perintah termux.\n\nclear\nPerintah dasar ini digunakan untuk membersihan jendela console\npwd\npwd (print working directory), digunakan untuk melihat posisis lokasi directory saat ini.\nls\ndigunakan untuk melihat /list file dan directory. gunakan ls -la untuk melihat informasi detail dari file dan folder\ncd\nDigunakan untuk nevigasi/pindah ke directory lain yang kita inginkan , gunakan cd .. untuk kebali ke 1 tingkat directory , gunakan cd ~ untuk menuju ke home directory\ncp\nDigunakan untuk mengkopi/nyalin File dan Folder .\ncp -avr /folder-asal /folder-tujuan untuk mengkopi folder dan isinya\nmv\nDigunakan Untuk memindahkan file dan folder tau bisa digunakan untuk merename jika file /folder mempunyai asal dan tujuan yang sama\nrm\nDigunakan untuk menghapus File.\nrm -rf namaFolder untuk menghapus folder dan isinya.\nrmdir\nDigunakan untuk menghapus Folder kosong .\nrmdir --ignore-fail-on-non-empty namafolder untuk menghapus folder yang tidak kosong\nchmod\nDigunakan untuk mengubah File /folder permission/privilage.\nchmod +x namaFolder untuk merubah permisin ke 775 atau rwx–x–x\nKode Perintah Aplikasi Termux Berbeda-Beda\nGaris besarnya kamu hanya perlu menghafal perintah pkg dan perintah operasional directory seperti diatas sebagai modal kamu bisa menggunakan termux.\n\nTapi perlu diingat setiap aplikasi di termux punya parameter sendiri-sendiri yang mungkin kamu harus belajar cara menggunakan dan menghafalkan parameter tersebut,perintah diatas sudah cukup membekalimu untuk mengexplore dan melangkah ke jenjang yang lebih tinggi.\n\nKode Perintah Untuk Menginstall dan Menjalankan Aplikasi Termux\nCara Menginstall Aplikasi Termux\nAda 3 caya yang bisa kamu lakukan untuk menginstall aplikasi di termux yaitu :\n\nDownload dan install aplikasi dari official software repository menggunakan perintah pkg atau apt (seperti kode diatas)\nDownload aplikasi yang dibuat khusus untuk termux dengan extensi *.deb dan menginstallnya menggunakan perintah $ dpkg -i nama_aplikasi.deb\nDownload aplikasi berupa script dari bahasa pemrograman interpreter seperti perl,ruby dan python\nCara Menjakankan Aplikasi Termux\nSecara umum cara menjalankan aplikasi di termux setelah kamu berhasil menginstall nya cukup dengan mengetikan nama dari aplikasi tersebut.\n\nTapi jika kamu ingin menjalankan aplikasi termux yang masih berupa script dengan extensi *.py (python),*.rb(ruby) ataupun *.pl(perl) maka kamu harus menginstall bahasa pemrograman tersebut untuk bisa menjalankan nya. install dengan perintah $ pkg install perl ruby python dan jalankan aplikasi yang berupa script dengan perintah $ perl script_mu.pl atau $ ruby script_mu.rb atau $ python script_mu.py\n\nMenggunakan Termux Untuk Bekerja\Mungkin kamu kesini belajar termux untuk hacking terutama untuk ngisengin orang ataupun berfikir untuk mbobol system,untuk orang profesional termux digunakan lebih dari itu.\n\nSaya sebagai IT admin sangat terbantu dengan adanya termux di HP android ku, saya bisa dengan mudah mengecek jaringan dan seluruh perangkat komputer yang ada di kantor pusat atau cabang menggunakan HP tanpa harus lama-lama menghidupkan laptop jika terjadi trouble.\n\nMenggunakan Termux Untuk Hacking\nPenggunaan komputer tidak terbatas begitu juga dengan termux,kamu bisa menggunakan nya sebagai tool atau platform untuk menjalankan aplikasi pentestool untuk kegiatan hacking.Ada beberapa hacking framework yang bisa kamu install dan gunakan untuk memudahkan dalam menemukan vulnerability ataupun membuat exploit.\n\nKESIMPULAN\nTermux pada dasarnya linux yang bisa kamu manfaatkan untuk tujuan apapun,tak ada batasan penggunaan termux karena bergantung pada kreatifitas dan kebutuhan pemakainya,ingat termux hanyalah alat,beda orang beda cara dan tujuan dalam memakainya.\n\nPerlu diingat!! menggunakan termux tidak akan menjadikan mu punya skill hacking instan,karena untuk menjadi seorang hacker perlu belajar banyak hal dalam bidang komputer"
print(menu)
print(menu2)
print(garis)

w = input("[+] PILIH SALAH SATU : ")
if w == "1":
    os.system("clear")
    print(menu)
    print(menu2)
    print(garis)
    print("[•] LOADING...")
    time.sleep(2)
    os.system("clear")
    os.system("pkg update && pkg upgrade -y")
    os.system("pkg install nano -y")
    os.system("apt update && apt upgrade -y")

elif w == "2":
    os.system("clear")
    print(menu)
    print(menu2)
    print(garis)
    time.sleep(5)
    print(lengkap)

elif w == "3":
    os.system("clear")
    print(menu)
    print(menu2)
    print(garis)  	
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(keys)
    os.system('termux-reload-settings')

elif w == "4":
    os.system("clear")
    print(menu)
    print(menu2)
    print(garis)
    time.sleep(1)
    print("[•] LOADING ...")
    time.sleep(3)
    os.system("cp -r login.py /$HOME")
    os.system("cd")
    os.system("nano login.py")

elif w == "5":
    os.system("clear")
    print(menu)
    print("[•] MEMBUKA WANGSAF ANDA...") 
    time.sleep(1)
    os.system("xdg-open https://wa.me/6281393668101?text=Hayuk%20mabar%20bro%20hahaha")

elif w == "6":
    sys.stdout

else:
    print("[!] LU BUTA KAH AJG!!!")
    time.sleep(1)
    os.system("python3 wiki.py")
