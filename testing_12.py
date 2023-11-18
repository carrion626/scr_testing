import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

# Input the keywords using 'Space'
keywords = input('What keywords are you searching for?').split()
key = ''

# Input type. Will search repositories by default if none of the other mentioned
types = input('What type are you searching for?\n-repositories?\n-issues?\n-wikis?\n')

for i in keywords:
    key += '+' + i

URL = f'https://github.com/search?q={key}&type={types}'


# Scraping website with the list of free proxies
resp = requests.get('https://www.sslproxies.org/')
soup1 = BeautifulSoup(resp.text, 'lxml')
proxies = soup1.find_all(name='td')

# Getting ip addresses and ports
pr_list = []
for p in proxies:
    p = p.getText()
    pr_list.append(p)

ip_address = pr_list[0::8]
ports = pr_list[1::8]

# Creates a list of proxies servers
proxy_servers = []

for i in range(len(ip_address)):
    proxy_servers.append(ip_address[i] + ':' + ports[i])

PROXY = {
    'proxies': [random.choice(proxy_servers), random.choice(proxy_servers)]
}


# Scraping GitHub
response = requests.get(url=URL, proxies=PROXY)
soup = BeautifulSoup(urlopen(URL), 'lxml')

list_of_urls = []
for tag in soup.find_all(class_='Link__StyledLink-sc-14289xe-0 fIqerb'):
    final = 'https://github.com'+tag.get('href')
    output = {
        'url': final,
    }
    list_of_urls.append(output)


print(list_of_urls)
