
import re
import pandas as pd
from pandas.core.frame import DataFrame
from pathlib import Path

Path('data/anno_xls').mkdir(exist_ok=True, parents=True)

dirpath = 'data/anno/'
fileids = [i for i in range(19, 36+1)]

writer = pd.ExcelWriter('data/anno_xls/19monthold36monthold.xlsx', engine='xlsxwriter')
for fileid in fileids:
    filepath = dirpath+ str(fileid) + '.txt'

    texts, annos, sentences = [], [], []
    with open(filepath, 'rt') as f:
        for line in f:
            for sentence in line.split('.'):
                parsed = re.findall ("\[\[(\w*)\]\]", sentence)
                if parsed:
                    text = re.sub("\[\[(\w*)\]\]", '', sentence)
                    anno = [a for a in parsed]
                    if anno:
                        sentences.append(sentence)
                        texts.append(text)
                        annos.append(anno)
                    # print(sentence)
                    # print(text)
                    # print(anno)
                    # print()

    df = pd.DataFrame({'Natural Language':texts, 'Extraction':annos, 'Annotated Sentence':sentences})
    # print(df)
    df.to_excel(writer, sheet_name=str(fileid)+'MonthOld', index=False)
writer.save()

# Merge into several sheets
writer = pd.ExcelWriter('data/anno_xls/multisheets.xlsx', engine='xlsxwriter')

for sheetid in range(0, 18+1):
    df = pd.read_excel('data/anno_xls/0monthold18monthold.xlsx', sheet_name=str(sheetid)+'MonthOld')
    df.to_excel(writer, sheet_name=str(sheetid)+'MonthOld', index=False)
    # print(df)
for sheetid in range(19, 36+1):
    df = pd.read_excel('data/anno_xls/19monthold36monthold.xlsx', sheet_name=str(sheetid)+'MonthOld')
    df.to_excel(writer, sheet_name=str(sheetid)+'MonthOld', index=False)
    # print(df)
writer.save()

# Merge into one sheets
writer = pd.ExcelWriter('data/anno_xls/onesheet.xlsx', engine='xlsxwriter')

source = []
df = DataFrame()
for sheetid in range(0, 18+1):
    df_read = pd.read_excel('data/anno_xls/0monthold18monthold.xlsx', sheet_name=str(sheetid)+'MonthOld')
    # print(df_read)
    df = df.append(df_read, ignore_index=True)
    # print(df)
    for _ in range(len(df_read)):
        source.append(str(sheetid)+'MonthOld.txt')
for sheetid in range(19, 36+1):
    df_read = pd.read_excel('data/anno_xls/19monthold36monthold.xlsx', sheet_name=str(sheetid)+'MonthOld')
    df_read = df_read.iloc[:, 0:2]
    # print(df_read)
    df = df.append(df_read, ignore_index=True)
    for _ in range(len(df_read)):
        source.append(str(sheetid)+'MonthOld.txt')
# print(source)
df['Source'] = source
print(df.head())
print(df.tail())
df.to_excel(writer, index=False)
writer.save()

