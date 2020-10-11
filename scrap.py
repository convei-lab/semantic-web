import requests
from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm

Path('data/raw').mkdir(exist_ok=True, parents=True)

print('Downloading raw data')
for i in tqdm(range(37)):
    month = str(i)
    if i <= 12:
        URL = 'https://www.thebump.com/baby-month-by-month/'+month+'-month-old-baby'
    else:
        URL = 'https://www.thebump.com/toddler-month-by-month/'+month+'-month-old'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    html = soup.find(id='main-col')
    texts = html.findAll(text=True)
    
    with open('data/raw/'+month.zfill(2)+'.txt', 'w') as f:
        f.write('\n'.join(texts))

import glob, os

os.chdir("./data/raw")

aggregated = ""
for file in sorted(glob.glob("*.txt")):
    with open(file, 'rt') as f:
        aggregated += f.read()

os.chdir("..")
Path('aggre').mkdir(exist_ok=True, parents=True)
with open('aggre/aggre.txt', 'wt') as f:
    f.write(aggregated)

