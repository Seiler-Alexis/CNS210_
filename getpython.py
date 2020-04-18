#! c:\Python3\python.exe


from bs4 import BeautifulSoup
import requests
import urllib
    
def FindRow(rows):

    line = 0
    for row in rows:
        if (str(row) == '<span class="release-date">April 6, 2013</span>'):
            if (str(rows[line + 1]) == '<span class="release-download"><a href="/downloads/release/python-274/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>'):
            
                for link in rows[line + 1].find_all('a'):
                    geturl = link.get('href')
                    downloadpage = requests.get('https://www.python.org' + geturl)
                    bsoup = BeautifulSoup(downloadpage.text, 'html.parser')
                    return bsoup
        line = line + 1

def FindLink(bsoup):
    getlinks = bsoup.find_all('td')
    linez = 0
    for getlink in getlinks:
        if (getlink.text == 'Windows x86-64 MSI installer'):
            for download in getlinks[linez].find_all('a'):
                downloads = download.get('href')
                urllib.request.urlretrieve(downloads, "AlexisSeiler-Python-2-7-4.msi")
                print("Completed")
        linez = linez + 1
def Main():
    url = 'https://python.org/downloads'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    rows = soup.find_all('span')
    bsoup = FindRow(rows)
    FindLink(bsoup)
Main()
