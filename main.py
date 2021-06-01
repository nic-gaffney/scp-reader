import shutil
import requests
from sys import argv
from bs4 import BeautifulSoup


if len(argv) < 2:
    print("Missing required armument: scp-number\nPlease enter a valid scp")


def set_num(num):
    num = str(num)
    if len(num) == 1:
        num = f'00{num}'
    elif len(num) == 2:
        num = f'0{num}'
    return int(num)


def get_scp(num):
    num = set_num(num)
    url = f'http://www.scpwiki.com/scp-{num}'
    page = requests.get(url+num)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='page-title').text.strip()
    page = soup.findAll(id='page-content')
    for item in page:
        object_class = item.find('strong', string="Object Class:").next_sibling.strip()
        scp = item.find('strong', string="Special Containment Procedures:").next_sibling.strip()
        desc = item.find('strong', string="Description:").next_sibling.strip()
        
    scp = {'title':title,
           'object_class':object_class,
           'containment':scp,
           'description':desc}
    
    return scp
        
