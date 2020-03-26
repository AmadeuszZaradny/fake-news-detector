import urllib.request
from bs4 import BeautifulSoup

UNWANTED_MARKUPS = ["script", "style"]


def extract_text_from_html(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)

    for script in soup(UNWANTED_MARKUPS):
        script.extract()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

