import requests
from bs4 import BeautifulSoup
import pprint

def scrape(webpage, page_num=1):
    i = 1
    links = []
    subtext = []
    while i <= page_num:
        website = webpage + str(i)
        response = requests.get(website)
        soup = BeautifulSoup(response.text, 'html.parser')
        links.extend(soup.select('.titleline'))
        subtext.extend(soup.select('.subtext'))
        i += 1
    return create_custom_hn(links, subtext)

def sort_stories(stories):
    sorted_stories = sorted(stories, key=lambda k: k['votes'], reverse=True) 
    return sorted_stories

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].find('a').get('href')
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({
                    'title': title,
                    'link': href,
                    'votes': points
                })
    return sort_stories(hn)

pprint.pprint(scrape('https://news.ycombinator.com/?p=', 1))