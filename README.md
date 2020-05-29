## Movies-Explorer
This is a web scraping project which provides the user with a list of all the movies currently being shown in the entered city, along with the show timings.

When you run the project in python environment, it will ask you to enter city name in which you want to search available movies. A new .txt file will be generated in the same folder with name **Movies_in_city**. Results will be saved in this file.

### Libraries/Modules Used:

* **Requests:** The requests module allows you to send HTTP requests using Python.The HTTP request returns a Response Object with all the response data (content, encoding, status, etc)

* **BeautifulSoup:** Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

### Code Explaination:

```
import requests
from bs4 import BeautifulSoup 
```

Here we are importing the request and beautifulsoup libraries.

```
code=requests.get(url)
```
Here code is a variable we are sending GET request to the specified URL and saving response returned by response object in code variable.

```
text=code.text  
```
Reading text from response object.

```
soup=BeautifulSoup(text,"html.parser") 
```
Soup is a Beautiful soup object. We are parsing the text to Beautifulsoup's constructor.

```
for link in soup.findAll('a',{'class':'__movie-name'}):
    title=link.get('title')                            
    link="https://in.bookmyshow.com"+link.get('href')  
    movie_name+=str(i)+"."+title+" "+link+"\n"       
```       
Here we are finding all <a> tags, storing title from movies, getting booking link and storing movie nanme title and booking link in one variable.

### Running the Project:

* Run command **python  movies.py**  (here movies.py is my file name)
