from bs4 import BeautifulSoup
import re
with open ("BMSLion.html") as file:
    s = BeautifulSoup(file)

values = []
keys = []
cellv = []
cellt = []

datas = s.findAll("div", class_ = "w3-right")

for i in datas:

    val = i.get_text()
    val = val.replace("\n", "")
    val = val.replace(" ", "")
    if val == "":
        val = "No value"
    values.append(val)


    a = i.find("h2")
    try:
        id = a.get('id')
        id = id.replace("\n", "")
        id = id.replace(" ", "")
        keys.append(id)


    except:
        id = "no field name"
        keys.append(id)

datas2 = s.find_all("td", class_ = "w3-right-align")

j = 0
for i in datas2:
    
    if j<13:
        cellv.append(i.get_text())
        j+=1
    else:
        cellt.append(i.get_text())

    


print(keys)
print(values)
print(cellv)
print(cellt)
