from lxml import html as htmlparser
from pathlib import Path
import requests

SRC_URL='https://sunlightfoundation.com/tools/expenditures/'
DEST_DIR = Path('wrangle', 'corral', 'fetched', 'sunlight', 'house')
DEST_DIR.mkdir(exist_ok=True, parents=True)

# Sample URL
# http://assets.sunlightfoundation.com.s3.amazonaws.com/expenditures/house/2015Q2-detail.csv

def main():
    hdoc = htmlparser.fromstring(requests.get(SRC_URL).text)
    for url in hdoc.xpath("//a[contains(@href, '/house/')]/@href"):
        if 'detail' in url:
            print("Downloading:", url)
            destpath = DEST_DIR / Path(url).name
            destpath.write_bytes(requests.get(url).content)
            print("Writing to:", destpath)

if __name__ == '__main__':
    main()



