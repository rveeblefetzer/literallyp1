"""Takes article information to prepare it for tweeting.

Separate scripts scrape newspaper websites for printed Page One articles.
This module takes the relevant headline, byline and deck; reformats long lines;
and returns tweet text and image.
"""


from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
import textwrap
import re


def reformat_stories():
    """Break long lines for tweet image."""
    with open('nyt_tweet_img.txt', 'r') as txt:
        listified = []
        for line in txt.readlines():
            for lil_line in textwrap.wrap(line, 80):
                listified.append(lil_line)
    with open('nyt_tweet_img.txt', 'w') as img_txt:
        for line in listified:
            if re.match(r'^[0-9]', line):
                line = '\n' + line
            img_txt.write(line)
            img_txt.write('\n')


def write_text_to_image():
    """Create and save image with other top stories."""
    lady_gray = (220, 220, 220)
    font_color = "#000"
    left_padding = 10
    font = ImageFont.truetype("Domine-Regular.ttf", 62)
    line_height = font.getsize('text')[1]
    num_lines = 35
    image_height = line_height * (num_lines + 1)
    image = Image.new("RGB", (2625, int(image_height)), lady_gray)
    draw = ImageDraw.Draw(image)
    with open('nyt_tweet_img.txt', 'r') as text:
        draw.multiline_text((left_padding, 10), text.read(), font_color,
                            font=font, spacing=35)
    img_expanded = ImageOps.expand(image, border=30, fill=lady_gray)
    img_resized = img_expanded.resize((500, int(image_height / 5.25)), Image.BICUBIC)
    img_resized.save("nyt_tweet.png")
