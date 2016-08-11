from lxml import html as htmlparser
from pathlib import Path
import requests

SRC_URL='https://sunlightfoundation.com/tools/expenditures/'
DEST_DIR = Path('wrangle', 'corral', 'fetched', 'sunlight', 'senate')
DEST_DIR.mkdir(exist_ok=True, parents=True)

# Sample URL
# http://assets-reporting.s3.amazonaws.com/1.0/senate_disbursements/113_sdoc17_senate_data_cleaned.csv

def main():
    hdoc = htmlparser.fromstring(requests.get(SRC_URL).text)
    for url in hdoc.xpath("//a[contains(@href, '/senate_disbursements/')]/@href"):
        print("Downloading:", url)
        destpath = DEST_DIR / Path(url).name
        destpath.write_bytes(requests.get(url).content)
        print("Writing to:", destpath)



if __name__ == '__main__':
    main()



