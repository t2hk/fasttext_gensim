import MeCab
import re, glob, sys
import pandas as pd

mecab = MeCab.Tagger('-d /usr/lib/mecab/dic/mecab-ipadic-neologd')

args = sys.argv
csv_dir = args[1]
wakati_file = args[2]

files = glob.glob(csv_dir + '/*.csv')

with open(wakati_file, 'w') as f:
  for file in files:
    df = pd.read_csv(file)

    col_name = '災害状況'
    if 'kikaisaigai' in file:
        col_name = '災害発生状況'

    print(file)
    sentences = df[col_name]

    for sentence in sentences:
        mecab.parse('')

        # 改行コードを含む場合があるため除去する
        sentence = ''.join(sentence.splitlines())
        node = mecab.parseToNode(sentence)
        sentence_nodes = []

        while node:
            word = node.surface
            sentence_nodes.append(word)
            #pos = node.feature.split(',')

            #print('{0}, {1}'.format(word, pos))

            node = node.next

        f.writelines(' '.join(sentence_nodes).strip() + '\n')
