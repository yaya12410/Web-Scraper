import requests
from bs4 import BeautifulSoup

url = "https://github.com/yaya12410" #The link to the page to be scraped
response = requests.get(url) #Get request to reach out to the server
html_code=response.content.decode()
# print(html_code)
soup = BeautifulSoup(html_code, 'html.parser')
data = soup.find('tbody')
print(data)

