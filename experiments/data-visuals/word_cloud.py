from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = "Outside the box creativity innovation technology future ideas solutions impact"
wc = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
