import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv
BryEmi= pd.read_csv('tags definitivo.csv', sep=";")['TagName']
word = ",".join(BryEmi)
readis = csv.reader(open('tags definitivo.csv','r',newline="\n"),delimiter= ';')
d = {}
count = 0
for k,v,l,o,j in readis:
    if count != 0:
        d[v] = float(l)
    count = count + 1
wordcloud = WordCloud(background_color='black',width= 1000, height=800,max_words=len(word)).generate_from_frequencies(frequencies=d)
plt.figure(figsize=(15,15))
plt.axis('off')
plt.imshow(wordcloud)
plt.show()