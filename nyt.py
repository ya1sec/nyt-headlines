from datetime import date
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen

today = date.today()
td = today.strftime("%m/%d/%y")

with open('timesheadlines.txt', 'a+') as filehandle:
    filehandle.write('\n' + 'NEW YORK TIMES HEADLINES FOR ' + td + '\n' + '\n')
print('\n' + 'NEW YORK TIMES HEADLINES FOR ' + td + '\n')


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
        headlineList = bs.findAll('h2')
        headlineList.pop(-1)
        headlineList.pop(-1)
        headlineList.pop(0)
        headlineList.pop(0)
        headlineList.pop(0)
        with open('timesheadlines.txt', 'a+') as filehandle:
            for headline in headlineList:
                print(headline.get_text())
                filehandle.write('%s\n' % headline.get_text())
        print("\n")
        print('Headlines written to timesheadlines.txt')
        print("\n")
    except AttributeError as e:
        return None
    return title


title = getTitle('https://www.nytimes.com')

if title == None:
    print('END')
else:
    print(title)
