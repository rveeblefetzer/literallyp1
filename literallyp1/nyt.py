#!/usr/bin python3.6
"""Scrape the New York Times website for Page One stories.

This module scrapes the nytimes.com webpage for front-page stories in the
printed edition, returning for details up to six articles. It grabs the
headline, byline and deck, as well as the text for the edition date.
"""

import requests
from bs4 import BeautifulSoup
import lxml
import os
from urllib.request import urlretrieve


def get_nyt_p1():
    """Get stories from NYT's print front page."""
    urlretrieve('http://www.nytimes.com/pages/todayspaper/index.html',
                'todays_nyt.txt')


def nyt_soupified():
    """Return today's Page One as Beautiful Soup object."""
    with open('todays_nyt.txt', 'r') as nytp1:
        soup = BeautifulSoup(nytp1, 'lxml')
        todays_nyt = soup.div
    return todays_nyt


def nyt_stories():
    """Take Page One and return article details."""
    soup = nyt_soupified()
    stories = soup.find_all('div', 'story')[:5]
    return stories


def get_nyt_date_text():
    """Return newspaper edition's date in a string."""
    todays_nyt = nyt_soupified()
    date = todays_nyt.find_all('h3', class_='sectionHeader')[0].text.split()
    date.insert(1, 'New')
    date.insert(2, 'York')
    nyt_tweet_date = (' ').join(date)
    return list([nyt_tweet_date])


def nyt_tweet_text():
    """Get details from top story for tweet text."""
    stories = nyt_stories()
    tweet_text = get_nyt_date_text()
    for string in stories[0].stripped_strings:
        tweet_text.append(string)
    tweet_text[3] = stories[0].find('a')['href']
    tweet = ''
    for line in tweet_text[:3]:
        tweet += line + '\n'
    tweet += tweet_text[3]
    return tweet


def other_nyt_stories():
    """Prepare other story details for tweet image."""
    stories = nyt_stories()
    # get date text and strip out just the date
    date_text = get_nyt_date_text()
    date = " ".join(date_text[0].split()[-3:])
    with open('nyt_tweet_img.txt', 'w') as out:
        out.write(f"Also on NYT's Page One for {date}:\n")
        counter = 2
        for story in stories[1:]:
            out.write(str(counter) + ': ')
            for string in story.stripped_strings:
                out.write(string)
                out.write('\n')
            out.write('\n')
            counter += 1
