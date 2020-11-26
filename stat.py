########################
#  TEXT PREPROCESSING  #
########################

import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from pathlib import Path
nltk.download('punkt')
Path('data/stat').mkdir(exist_ok=True, parents=True)

file_content=open("data/aggre/aggre.txt").read()

# Convert text to lowercase
result = file_content.lower()
# Remove numbers
result = re.sub(r'\d+', '', result)
# Remove punctuation
result = result.translate(str.maketrans("","", string.punctuation))
# Remove whitespaces
result = result.strip()
#Remove stop words
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(result)
result = [i for i in tokens if not i in stop_words]


########################
#      WORD CLOUD      #
########################
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = int(360.0 * 45.0 / 255.0)
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

    return "hsl({}, {}%, {}%)".format(h, s, l)

wordcloud = WordCloud(font_path = r'/usr/share/fonts/NanumGothic.ttf',
                            stopwords = STOPWORDS,
                            background_color = 'white',
                            width = 1200,
                            height = 1000,
                            color_func = random_color_func
                            ).generate(file_content)

plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('data/stat/wordcloud.png')
plt.show()

########################
#      WORD COUNT      #
########################
from collections import Counter
import pandas as pd
wordcount = Counter(result)
for item in wordcount.items(): 
    print("{}\t{}".format(*item))

df = pd.DataFrame.from_dict(wordcount, orient='index', columns=['Count']).reset_index()
df = df.sort_values(by='Count', ascending=False)
df.to_csv("data/stat/wordcount.csv")