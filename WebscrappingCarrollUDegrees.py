## pip install beautifulsoup4
## pip install requests

## import module
import requests
import bs4

# Generate the URL
url = "https://www.carrollu.edu/academics/undergraduate-programs"

# get the web page
request_result = requests.get(url).text
#print(request_result)

# Parse the HTML
soup = bs4.BeautifulSoup(request_result,"html.parser")

# find the class = "two-col-list"
temp = soup.find_all("ul", class_='two-col-list')
print(temp)

majors = temp[0]

print('MAJORS AT CARROLL UNIVERSITY')
for listitem in majors.find_all('li'):
    for atag in listitem.find_all('a'):
        print(atag.text)
minors = temp[2]
print()
print()
print('MINORS AT CARROLL UNIVERSITY')
for listitem in minors.find_all('li'):
    for atag in listitem.find_all('a'):
        print(atag.text)
