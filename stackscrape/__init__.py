"""
stackscrape.

Usage:
  stackscrape [-s SITE] [-t TAG] [-f TEXT] [-d DAYS] [-n NUM] [-o OUT] [-m] [-S]
  stackscrape -h | --help
  stackscrape --version

Get questions and accepted answers from a StackExchange site.

Options:
  -s SITE --site=SITE     Which StackExchange site to query. [default: stackoverflow]
  -t TAG --tag=TAG        Fetch questions tagged with the given TAG.
  -f TEXT --filter=TEXT   Fetch questions containing the given TEXT in the their title.
  -d DAYS --days=DAYS     How many days back to go. [default: 365]
  -n NUM --num=NUM        Max number of items to fetch. [default: 1000]
  -o OUT --out=OUT        Save results to file OUT.
  -m --merge              Merge title and question into one field.
  -S --score              Include scores in output.
  -h --help               Show this screen.
  --version               Show version.

"""

__version__ = '0.4'

from docopt import docopt, DocoptExit
from .stackscrape import get_qa


def main():
    arguments = docopt(__doc__, version=__version__)
    site = arguments['--site']
    tag = arguments['--tag']
    text = arguments['--filter']
    days = int(arguments['--days'])
    num = int(arguments['--num'])
    out = arguments['--out']
    merge = bool(arguments['--merge'])
    score = bool(arguments['--score'])
    get_qa(site, tag, text, days, num, out, merge, score)
    
