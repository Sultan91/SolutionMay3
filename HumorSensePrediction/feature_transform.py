'''

https://github.com/Phylliida/Dialogue-Datasets/blob/master/BNCCorpus.txt
https://www.kaggle.com/abhinavmoudgil95/short-jokes
Loading two raw datasets, one for normal text, one for jokes
'''

from model import get_pool_embed
import pandas as pd

limit = 400# no of rows
jokes_df = pd.read_csv("dataset/shortjokes.csv")
jokes_df.columns = ['ID', 'text']
jokes_df['class'] = 1
jokes_df['text'] = jokes_df['text'].replace('"', '', regex=True)
del jokes_df['ID']
jokes_df = jokes_df[:limit]

norm_df = pd.read_table("dataset/BNCCorpus.txt")
norm_df.columns = ['text']
norm_df['class'] = 0
norm_df = norm_df[:limit]
print(jokes_df.shape)
print(norm_df.shape)
train = pd.concat([jokes_df, norm_df], ignore_index=True)

transformed_df = []
for t in train['text']:
    temp = get_pool_embed(t)
    transformed_df.append(temp.tolist())
transformed_df = pd.DataFrame(transformed_df, columns=['feature'])
transformed_df['class'] = train['class']
transformed_df.to_pickle('train_data.pkl')


