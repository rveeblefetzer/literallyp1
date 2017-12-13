"""Tweet lead story from newspaper front pages and image of other top stories.

Separate modules scrape newspaper websites for articles printed on Page One,
and another module prepares text and images for tweets. This module takes each
daily top story information (headline, byline and deck) and tweets from user
account @literallyp1.
"""

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import tweepy
from nyt import nyt
import imagize


def get_nyt_tweet_text():
    """Return NYT top story details."""
    nyt.get_nyt_p1()
    nyt_text = nyt.nyt_tweet_text()
    return nyt_text


def get_nyt_tweet_image():
    """Save details of other top stories in an image."""
    nyt.other_nyt_stories()
    imagize.reformat_stories()
    imagize.write_text_to_image()


def send_daily_nyt_tweet():
    """Take tweet text and image and update status."""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    nyt_text = get_nyt_tweet_text()
    get_nyt_tweet_image()
    api.update_with_media('nyt/nyt_tweet.png', nyt_text)


if __name__ == "__main__":
    send_daily_nyt_tweet()
