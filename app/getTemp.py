import requests
from bs4 import BeautifulSoup
headers = {
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.4.677 Yowser/2.5 Safari/537.36",
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
  }

def TempToday(city): 
  URL = 'https://sinoptik.ua/погода-' + city.lower().replace(" ", "-")
  req = requests.get(url=URL, headers=headers)
  # print(req.headers)
  # with open("index.html", "w", encoding="utf-8") as file:
  #   file.write(req.text)
  if req != None:
    soup_first = BeautifulSoup(req.text, "lxml")
    try:
      city = soup_first.find("div", class_="wVlV1Xy9").text
      temp = soup_first.find("p", class_="_6fYCPKSx").text
      # with open("index.html", "w", encoding="utf-8") as file:
      #   file.write(soup.prettify())
      return city, temp
    except AttributeError:
      return "Place not found"
  else:
    return f"Not found {URL}"


