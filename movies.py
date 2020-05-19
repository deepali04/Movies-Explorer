import requests                #For making request to a web page and print response text                                                                 
from bs4 import BeautifulSoup  #Python library for web scraping (for puling data out of tml and xml file)


def movies_in_theatre(url):
    
    code=requests.get(url)                          #Response Object (code) --- sending GET request to specified URL
    text=code.text                                  #Reading text from response object
    soup=BeautifulSoup(text,"html.parser")          #Beautiful soup object (soup) --- parsing it to Beautifulsoup constructor
    movie_name="Movies_near_me @BookmyShow"+"\n\n"  
    i=1
    for link in soup.findAll('a',{'class':'__movie-name'}):
        title=link.get('title')
        link="https://in.bookmyshow.com"+link.get('href')
        movie_name+=str(i)+"."+title+" "+link+"\n"
        i+=1

    fw = open('Movies_in_my_city.txt', 'w')
    fw.write(movie_name)
    fw.close()

city=input("Enter a valid city name: ")
movies_in_theatre("https://in.bookmyshow.com/"+city+"/movies")
