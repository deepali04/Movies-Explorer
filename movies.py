import requests                #For making request to a web page and print response text                                                                 
from bs4 import BeautifulSoup  #Python library for web scraping (for puling data out of tml and xml file)


def movies_in_city(url):
    
    code=requests.get(url)                          #Response Object (code) --- sending GET request to specified URL
    text=code.text                                  #Reading text from response object
    soup=BeautifulSoup(text,"html.parser")          #Beautiful soup object (soup) --- parsing it to Beautifulsoup constructor
    movie_name="Movies_near_me @BookmyShow"+"\n\n"  
    i=1
    for link in soup.findAll('a',{'class':'__movie-name'}):  # finding all (<a> tag) movie names
        title=link.get('title')                              # storing title
        link="https://in.bookmyshow.com"+link.get('href')    # getting booking link
        movie_name+=str(i)+"."+title+" "+link+"\n"           # storing movie nanme title and booking link at one place
        i+=1

    fw = open('Movies_in_city.txt', 'w')         # Creating and opening a file named Movies_in_my_city.txt in write mode
    fw.write(movie_name)                            # writing movie_name variable (having all data) in this file
    fw.close()                                      #closing the file

city=input("Enter City : ")
movies_in_city("https://in.bookmyshow.com/"+city+"/movies") #Passing URL to the function
