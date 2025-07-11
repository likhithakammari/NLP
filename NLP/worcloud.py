from wordcloud import WordCloud
import matplotlib.pyplot as plt

text="""Machine Learning,DeepLearning and Natural Language Processing are following the better algorithm playing a key role  in AI concepts  Machine Learning,DeepLearning and Natural Language Processing are following the better algorithm playing a key role  in AI concepts"""
wordcloud=WordCloud(width=800,height=400,background_color='white').generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.show()

