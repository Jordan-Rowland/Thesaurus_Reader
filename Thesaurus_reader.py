#! python3
# Scrape Thesaurus.com for synonymous nouns

import requests, bs4, sys

search = sys.argv[0] # command argument for word to search
url = f'http://www.thesaurus.com/browse/{search}?s=t'

def thesaurus():
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    elems = soup.select('#filters-0 > div.relevancy-block > div') # selector for words returned
    return elems[0].text.strip() 

words = thesaurus()
words = words.replace('star', '').replace('\n\n', ' ') # gets rid of all the unneeded characters like spaces and 'star' added to each word

print(words)
