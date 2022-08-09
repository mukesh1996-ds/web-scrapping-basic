'''
If you want to scrap a website we need to follow these steps:
1. Using any API
2. HTML web scrapping using some tools like bs4

step 1:
To start with we need to install the following liberary in the enviroments
* pip install requests
* pip install bs4
* pip install html5lib 
'''
# import all the properties

from turtle import title
import requests
from bs4 import BeautifulSoup

# Giving the URL that we want to scrap
url = "https://www.paramount.com/"

# step 2: Get the html

r = requests.get(url)
htmlContent = r.content
# print(htmlContent) # I will be getting all the html page source code in your terminal.

# step3: Parse the html

soup = BeautifulSoup(htmlContent,'html.parser')
# print(soup) # Scrap out but there will not be any indendation
# print(soup.prettify) # scrap out with good indentaion

# Step4: HTML tree traversal 

# Commonly used type of objects:
# 1. Tag
# 2. Navigable string
# 3. Beautiful soup objects
# 4. Comment

# Get the title of the html page

title = soup.title
print(type(soup))
print('')
print(title) # Title of the page
print('')
print(type(title)) # Tag of the page
print('')
print(type(title.string)) # navigable string 
print('')

# get all the paragraph from the page
paras = soup.find_all('p')
# print(paras)
print('')

# get ancor tags 
anchors = soup.find_all('a')
# print(anchors)
print('')


# to get the first paragraph
print(soup.find('p')) # o/p => The leading global brand in entertainment 

# to get the class of any html page
print(soup.find('p')['class'])

# find all the element with class lead
print(soup.find_all('p', class_='lead'))

# get the text from the web page

print(soup.find('p').get_text()) # get the text out of paragraph

# to get complete text with out any tags
print(soup.get_text()) 

# get all the links on the page
all_links = set()
for link in anchors:
    if (link.get('href') != '#'):
        linkText = url + link.get('href')
        all_links.add(link)
        print(linkText)
        

