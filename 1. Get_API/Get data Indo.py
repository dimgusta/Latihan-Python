import json
from urllib import request

# tentukan url endpoint
url = "https://indonesia-covid-19.mathdro.id/api/provinsi"

# lakukan http request ke server
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())


# cetak hasil parsing data
for covid in data['data']:
# melakukan perulangan dimana var covid merupakan type var dict dalam json dan data['data'] merupakan data array keseluruhan yang akan di ulang 
# var covid merupakan nilai perulangan yang terurut dari nomor 1 sampai terakhir dalam kode json
    print("-",{covid['provinsi']})
    print("Kasus", {covid['kasusPosi']})
    print("Sembuh", {covid['kasusSemb']})
    print("Mati", {covid['kasusMeni']})

# https://medium.com/@durgaswaroop/json-parsing-with-python-15a41c6fe03a
# https://www.petanikode.com/python-json/
