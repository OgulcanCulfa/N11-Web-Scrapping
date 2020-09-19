import requests
from bs4 import BeautifulSoup

# url declaration

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar?q=notebook&m=Dell"


# library initialization

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

# scrapping the necessary infos

liste = soup.find("div", {"class":"listView"}).find_all("li", {"class":"column"})


# add price infos into the list

new_priceList = []

for prices in liste:
    
    new_price = prices.find("ins").text.replace(" ","").strip().replace("\n"," ").split('",')
    new_priceList.append(new_price)
    

# create a txt file and write the datas that we scrapped from website 


file = open("dell computer prices.txt", "x")
for files in new_priceList:
    file.write("%s\n" % files)



    
    
    


        
    
    




