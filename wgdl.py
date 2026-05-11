import bs4
import os
import requests
import sys
import argparse

USAGE = """Usage: wgdl [-d <target directory] <board/code>
This downloads all media from 4chan.org/<board>/thread/<code>, optionally to
the specified directory"""

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


parser = argparse.ArgumentParser(
        prog="wgdl",
        description="Download images from a 4chan thread",
        epilog="")

parser.add_argument("board", help="the short name for the board to download from")
parser.add_argument("thread", help="code of the thread to downlaod from")
parser.add_argument("-d", "--dir", help="download directory")

# exit if no code was provided
if len(sys.argv) < 3:
    parser.print_help()
    sys.exit()

args = parser.parse_args()
link = "https://boards.4chan.org/" + args.board + "/thread/" + args.thread

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
dirname = args.dir or path_string(title if title != '' else 'wg')
os.mkdir(dirname)
print("Downloading images to " + dirname)
draw_progress(0, total)
for num, media_file in enumerate(media):
    res = requests.get(media_file)
    with open(dirname + "/media" + str(num), "wb") as fp:
        for chunk in res.iter_content(10000):
            fp.write(chunk)
    draw_progress(num+1, total)

sys.stdout.write("\n")
