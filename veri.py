from bs4 import BeautifulSoup

with open ("BMSLion.html") as file:
    s = BeautifulSoup(file)

datas = s.findAll("div", class_ = "w3-right")

for i in datas: 
    print(i.get_text())
    a = i.find("h2")
    try:
        id = a.get('id')
        print(id)
    except:
        print("no field name")
    print("--------------------------------------")

