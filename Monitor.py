from time import time, sleep

import requests
from bs4 import BeautifulSoup
from support_funcs import *

webhook = "https://discordapp.com/api/webhooks/699562707111903252/fzra2OyRlmUAgD1REShp8k2xomlFHZRDR7D7-tY7juN9LQ8TGZ405UNOG3W-xFOPT2dO"


def compare_links(links, old_links, webhook):
    new_links = []
    for link in links:
        if link in old_links:
            pass
        else:
            new_links.append(link)
            old_links.append(link)
            PagingDiscordServer(webhook, "https://www.olx.pl"+link)
            update_old_links(link)
    return new_links

def update_old_links(link):
    with open('old_links.txt', 'a') as file:
        file.write(link + '\n')

def read_old_links():
    with open('old_links.txt') as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def main():
    url = 'https://www.olx.pl/d/elektronika/tv/telewizory/warszawa/q-telewizor/?search%5Bdist%5D=30&search%5Border%5D=created_at:desc&search%5Bfilter_enum_state%5D%5B0%5D=damaged'
    webhook = "https://discordapp.com/api/webhooks/699562707111903252/fzra2OyRlmUAgD1REShp8k2xomlFHZRDR7D7-tY7juN9LQ8TGZ405UNOG3W-xFOPT2dO"
    old_links = read_old_links()
    while True:
        start = time()
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        x = soup.findAll("div", {"data-cy":"l-card"})
        for item in x:
            links.append(item.find("a")["href"])
        new_links = compare_links(links, old_links, webhook)
        stop = time()-start
        print(f"Status odpowiedzi: {response.status_code}, Nowe linki: {len(new_links)}, Czas: {stop}")
        sleep(10)

while True:
    try:
        main()
    except:
        PagingDiscordServer(webhook, "Problem z botem")
        sleep(100)
        main()