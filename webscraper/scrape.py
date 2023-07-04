import requests
from bs4 import BeautifulSoup
import pprint

#  Gets the Titles and Links to the Articles of the most upvoted Elements from hackernews


res1 = requests.get('https://news.ycombinator.com/news')  # get first url we want to parse
soup1 = BeautifulSoup(res1.text, 'html.parser')  # creates a BeautifulSoup object for the first page
links1 = soup1.select('.titleline') # selects all elements with class titleline from the first page
subtexts1 = soup1.select('.subtext') # selects all elements with class subtext from the first page

res2 = requests.get('https://news.ycombinator.com/news?p=2')  # get second url we want to parse
soup2 = BeautifulSoup(res2.text, 'html.parser')  # creates second  BeautifulSoup object
links2 = soup2.select('.titleline')  # selects all elements with class titleline from second Page
subtexts2 = soup2.select('.subtext')  # selects all elements with class subtext from second Page

links1.extend(links2)  # combines the two lists (from the two pages)
subtexts1.extend(subtexts2)  # combines the two subtext lists (from the two pages)


def sort_stories_by_votes(hnlist):  # sorts the list by votes in decreasing order
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):  
    hn = []
    for index, item in enumerate(links):

        title = item.getText()
        href = item.a.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            point = int(vote[0].getText().replace(' points', ''))
            if point > 99:
                hn.append({'title': title, 'link': href, 'votes': point})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links1, subtexts1))  # prints the list of dictionaries

