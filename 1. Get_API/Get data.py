import json
from urllib import request

# tentukan url endpoint
#url = "http://127.0.0.1/program/menampilkan_table_counter_json2.php" #merupakan link API yang akan di baca

url = "https://covid19.mathdro.id/api/countries/indonesia"

# lakukan http request ke server
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())
#print (data) #menampilkan data yang diambil

# cetak hasil parsing data
confirm = data['confirmed']['value']
recovery = data['recovered']['value']
death = data['deaths']['value']

print("Jumlah = ", confirm)
print("Sembuh = ", recovery)
print("Meninggal = ", death)


# https://medium.com/@durgaswaroop/json-parsing-with-python-15a41c6fe03a



