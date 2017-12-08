literallyp1
===========

.. image:: https://travis-ci.org/rveeblefetzer/literallyp1.svg?branch=master
    :target: https://travis-ci.org/rveeblefetzer/literallyp1
    :alt: Latest Travis CI build status

A Twitter bot that scrapes, tweets top stories from certain newspaper front pages

This project was borne from a conversation with an old journalist friend about news
cycles, social media and feeds. You don't have to be a newspaper person to know
that Page One is a big deal; plenty of movie tropes show reporters scrambling to
get their story on the front, and a roomful of editors arguing over placement. For the
outlets that take it seriously, it's a big decision to distill the day's events
into the most important that will fit on one page.

Of course, these headlines are still out there in the different feeds. But the
labor and human decision-making that go into the day's top stories is even more
obscured, simply because most people aren't looking. This bot aims to simply
tweet the top story, with an image of the next several stories' details.

It grabs top stories from newspaper websites that have their print front page
available online and tweets the top story's headline, byline and link, along with a
.png image of the headline, byline and deck of up to the next five page-one
stories.

Right now, it's only for The New York Times, and that's getting tweeted out
`here <https://twitter.com/literallyp1>`_.

Usage
-----

Get some keys and access tokens from Twitter, and hide them in a good spot. I
put mine in a gitignored file called config.py and import the variables.

Currently, running ``python3 literallyp1.py`` will tweet the top six stories from
the from the front page of The New York Times. More newspapers to come (TK, for
the news nerds); see the issues and pitch in if you can.

To send tweets regularly without manually running that command, set up a cron
job. I don't know when the Times updates its "Today's Paper" webpage, but 4am
EST is a good bet. Up to you if you want to do this from an
always-on-and-connected computer, or from a cloud service like Heroku

For a good how-to on getting Twitter keys and setting this up on Heroku, see
`this post <https://briancaffey.github.io/2016/04/05/twitter-bot-tutorial.html>`_
by Brian Caffey.

Molly White has `another good blog post
<http://blog.mollywhite.net/twitter-bots-pt2/>`_ on setting up a Twitter bot
that also explains cron jobs.

Installation
------------

Clone repo and run ``pip install -r requirements.txt``.

Requirements
^^^^^^^^^^^^

This package needs requests, BeatifulSoup and lxml to get the story details;
Pillow to make the tweet image; and tweepy to do the tweeting.

Licence
-------

Authors
-------

`literallyp1` was written by `Rick Valenzuela <rv@rickv.com>`_.
