import requests
import re
from bs4 import BeautifulSoup
import sched, time


def job_search(sc):
    print("Searching...")
    #define job source URL
    URL = 'https://jobs.lever.co/izotope'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    #define keyword to look for
    results = soup.body.findAll(text=re.compile('Engineer'), limit=10)

    #defines connection / http error
    print(results)
    s.enter(5, 1, job_search, (sc, ))



if __name__ == '__main__':
    s = sched.scheduler(time.time, time.sleep)
    #rate of repeater
    s.enter(5, 1, job_search, (s))
    s.run()
