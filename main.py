# Import library yg dibutuhkan
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'csv/kata.csv', encoding="latin-1")

comment_words = "" #variabel kosong utk menyimpan kata-kata
stopwords = set(STOPWORDS) # mengambil modul yang sudah di import

# interaksi melalui dataframe
for val in df.CONTENT:
    val = str(val)
    tokens = val.split()

    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=1366, height=768, background_color="white", stopwords=stopwords, min_font_size=10).generate(comment_words)

# Untk menampilkan data
plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud)
plt.axis('off') # menghilangkan sumbu x dan y
plt.tight_layout(pad=0) # memastkikan tata letak

plt.show() # menampilkan pd layar