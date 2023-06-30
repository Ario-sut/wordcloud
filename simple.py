from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("words.txt", "r") as f:
    text = f.read()

wordcloud = WordCloud(width=1366, height=673, background_color='white', min_font_size=10).generate(text)

plt.figure(figsize=(8,8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off') # menghilangkan sumbu x dan y
plt.tight_layout(pad=0) # memastkikan tata letak
plt.show() # menampilkan pd layar