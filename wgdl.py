import bs4
import os
import requests
import sys

USAGE = """Usage: wgdl <board/code>
This downloads all media from 4chan.org/<board>/thread/<code>"""

MEDIA_TYPE = ("png", "jpg", "jpeg", "webp", "webm", "gif", "mp4")

# TODO: write a terminal interface that lets user select a thread directly from terminal, without the need to use a browser


def draw_progress(actual: int, total: int):
    sys.stdout.write("\r")
    sys.stdout.write("Progress: [" + str(actual) + " of " + str(total) + "]")
    sys.stdout.flush()


def path_string(title: str) -> str:
    sanitized = ""
    for c in title:
        if c in [ " ", "/", "\\" ]:
            sanitized += "_"
        else:
            sanitized += c
    return sanitized


# exit if no code was provided
if len(sys.argv) < 2:
    sys.exit(USAGE)

[ board, thread ] = sys.argv[1].split("/", 1)
link = "https://boards.4chan.org/" + board + "/thread/" + thread

res = requests.get(link)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

title = soup.select(".subject")[0].getText()

media = set()
anchors = soup.select("a")
for a in anchors:
    href = a.get("href")
    if "http" not in href:
        href = "https:" + href
    for it in MEDIA_TYPE:
        if href.endswith(it):
            media.add(href)
            break

total = len(media)
dirname = path_string(title if title != '' else 'wg')
os.mkdir(dirname)
draw_progress(0, total)
for num, media_file in enumerate(media):
    res = requests.get(media_file)
    with open(dirname + "/media" + str(num), "wb") as fp:
        for chunk in res.iter_content(10000):
            fp.write(chunk)
    draw_progress(num+1, total)

sys.stdout.write("\n")
