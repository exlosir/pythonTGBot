from bs4 import BeautifulSoup
import urllib.request

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def get_weather(html):
    soup = BeautifulSoup(html)
    value_temp = soup.find('span', class_='temp__value').text
    location = soup.find('div', class_="location__title-wrap").find('h1', class_="title title_level_1")
    time = soup.find('time', class_="time fact__time").text
    curr_location = str(location.contents[0]) + "" + str(location.find('span', class_="string-with-sticky-item").contents[0])
    return str(time) + ". "+ curr_location + " " + str(value_temp)
