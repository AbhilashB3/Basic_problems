import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.google.com/search?q=nz+vs+ind&rlz=1C1RXQR_enIN1222IN1222&oq=&gs_lcrp=EgZjaHJvbWUqCQgBECMYJxjqAjIJCAAQLhgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQw1OTAzNzEzNWowajeoAgiwAgHxBSTWYMWvm0Rg&sourceid=chrome&source=chrome.ob&ie=UTF-8")
htmlpage=response.text
b=BeautifulSoup(htmlpage)
#print(b.text)
#print(b.select(''))
#print(b.find('AA'))
print(b.find_all('AA'))