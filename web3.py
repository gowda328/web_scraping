import requests
from bs4 import BeautifulSoup
import time

print('put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    ht = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit'
                      '&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(ht, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for job in jobs:
        publish = job.find('span', class_='sim-posted').span.text
        if 'few' in publish:
            com = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                print(f"Company name:{com.strip()}")
                print(f"Required skills:{skills.strip()}")
                print(f'More_info:{info}')
                print('-----------------------------------------------------------------------------')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes.....')
        time.sleep(time_wait*60)