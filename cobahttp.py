#import library HTTP
import http.client 

#inisiasi koneksi HTTP, membuat threehand syaking
conn = http.client.HTTPConnection("filkom.ub.ac.id")  


# kirim request
conn.request("GET","/")
resp = conn.getresponse()
#cetak response

print(resp.status)  #melihat statusnya 200 atau yang lain
print(resp.read()) #melihat bodynya

