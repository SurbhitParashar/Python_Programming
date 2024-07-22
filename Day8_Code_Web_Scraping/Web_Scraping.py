import requests
from bs4 import BeautifulSoup

#Step 1: Get the html
url="https://opportunity.linkedin.com/skills-for-in-demand-jobs"
req=requests.get(url)
html_content=req.content
# print(html_content)

#Step 2: Parsing the HTMl
soup = BeautifulSoup(html_content,'html.parser')
# print(soup.prettify)

#step 3: HTML tree traversal

# commonly used type of objects
# 1. tag
# 2. navigable string
# 3. BeautifulSoup
# 4. comment
# markup="<p><!--this is a comment --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p.string)
# print(type(soup2.p.string))
# exit()

#Get the title of the page
# title=soup.title 

# print(type(soup))
# print(title)
# print(type(title))
# print(title.string)
# print(type(title.string))

#Get all the paragraph from the page 
paras = soup.find_all('p')
# print(paras)

#Get all the anchor tags from the page 
anchors = soup.find_all('a')
# print(anchors)

set_=set()
#get all the links 
for link in anchors:
    set_.add(link.get('href'))
    # print(link.get('href'))
    
# Getting first para
para1=soup.find('p')
# print(para1)
# print(soup.find('p')['class']) #to get class in first para

#get all the element with having a particular class
# print(soup.find_all('p',class_='banner-subheadline'))

#get the text from the tag
# print(soup.find('p').get_text())
# print(soup.get_text())

# navsupportedcontent = soup.find(id="")
