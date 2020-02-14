import requests

url1 = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
url2 = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
data1 = requests.get(url1)
data2 = requests.get(url2)
kodeprovinsiraw = data1.json()
kodepos = data2.json()

kodeprovinsikeys=kodeprovinsiraw.keys()
kodeprovinsivalues=kodeprovinsiraw.values()

kodeprovinsi = dict((zip(kodeprovinsivalues,kodeprovinsikeys)))

kodeprovinsidilan = str(kodeprovinsi['BANTEN'])
kodeprovinsimilea = str(kodeprovinsi['JAWA BARAT'])

for i in kodepos[kodeprovinsidilan] :
    if i['urban'] == "SAMPORA" and i["sub_district"] == "CISAUK" and i["city"] == 'TANGERANG' :
        kodeposdilan = i["postal_code"]


for j in kodepos[kodeprovinsimilea] :
    if j['urban'] == "CITARUM" and j["sub_district"] == "BANDUNG WETAN" and j["city"] == 'BANDUNG' :
        kodeposmilea = j["postal_code"]

apikey ='9mkHDVaN6FSy48k6Govz8DU619IdmJloCCUpISJ6ZbZZMiHbAG7uH9LhAad9ROqC'
url3 = f'http://www.zipcodeapi.com/rest/{apikey}/distance.json/{kodeposdilan}/{kodeposmilea}/km'
data3 =  requests.get(url3)
jarak = data3.json()

print(f'Kode Pos lokasi Dilan adalah {kodeposdilan}')
print(f'Kode Pos lokasi Milea adalag {kodeposmilea}') 
print(f'Jarak Dilan & Milea adalah {jarak["distance"]} km')    