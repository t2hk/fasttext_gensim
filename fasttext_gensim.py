from gensim.models.wrappers.fasttext import FastText

model = FastText.load_fasttext_format('fasttext_model')

vector = model.wv["カバー"]
word = model.most_similar([ vector ], [], 10)
print(word)

print("------------")

vector = model.wv["フォークリフト"]
word = model.most_similar([ vector ], [], 10)
print(word)

print("------------")

vector = model.wv["ブルドーザー"]
word = model.most_similar([ vector ], [], 10)
print(word)

