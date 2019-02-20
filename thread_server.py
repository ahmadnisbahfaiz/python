#import socket
import socket
#import library threading
import threading

#inisialisasi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind
sock.bind(("0.0.0.0", 7777))
#listen
sock.listen(100)  #Berapa jumlah koneksi yang dapat di handle dalam satu koneksi

#fungsi untuk menghandle satu thread
#(fungsi yang di jalankan dalam sebuah thread)
#parameter fungsi ini adalah variabel koneksi ke client

def handle_thread(conn): #parameternya koneksi karena jika terdapat koneksi baru akan dibuatkan satu thread
    while True : #Agar Threadnya tidak mati
        try :
             #terima data yang di kirimkan oleh client
             data = conn.recv(100) #berapa data yang mau kita baca dari buffer
             #Decode jdai String
             data = data.decode("ascii")
             data = "OK " + data
             #kirim lagi ke client
             conn.send(data.encode("ascii"))
        #jika terjadi pemutusan koneksi oleh client
        #tangkapn exceptionnya, kemudian tutup koneksi dan brea
        except(socket.error):
                conn.close()
                break

#menggunakan "while True"(agar  koneksinya dapat berulang-ulang)
while True :
    #Terima permintaan koneksi
    conn, client_addr = sock.accept()  #tidak harus nama conn, dan client_addr
    #buat thread baru, panggi fungsi handle_thread
    t = threading.Thread(target = handle_thread, args = (conn,))
    #start threadnya
    t.start()