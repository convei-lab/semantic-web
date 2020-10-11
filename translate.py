from googletrans import Translator
from pathlib import Path
from tqdm import tqdm
translator = Translator()
def translate(text):
    try:
        result = translator.translate(text, src='en', dest='ko')
        if result:
            return result.text
        else:
            return None
    except Exception as e:
        print(e, text)

Path('data/translated').mkdir(exist_ok=True, parents=True)

with open('data/aggre/aggre.txt') as f:
    lines = f.readlines()

results = []
for line in tqdm(lines):
    translated_line = translate(line)
    if translated_line:
        results.append(translated_line)

with open('data/translated/translated.txt', 'wt') as f:
    f.write('\n'.join(results))