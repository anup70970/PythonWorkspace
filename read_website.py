import requests
import urllib.request
import time
import argparse

def read_web():
    url = 'https://www.google.dk'
    rendr = requests.get(url)

    print(rendr.status_code , "OK")

def save_url():
    link = 'https://www.google.dk'
    rendr = urllib.request.urlopen(link)
    mydata = rendr.read()
    with open('webpage_read.html','wb') as file:
        file.write(mydata)


if __name__=='__main__':
    print('appending website content to .html file after 5 sec')
    time.sleep(5)
    save_url()
    print('checking if status code for website is 200 OK')
    read_web()
