from wordcloud import WordCloud
import matplotlib.pyplot as plt

my_name="likhitha kammari"
hashtags=["#Panilenii papa","#student of waste clg","#friends are best","#dont be to do","#Panilenii papa","#student of waste clg","#friends are best","#dont be to do","#Panilenii papa","#student of waste clg","#friends are best","#dont be to do"]
text=(my_name+' ')*100+' '.join(hashtags*5)
wordcloud=WordCloud(width=1000,height=500,background_color='white',colormap='viridis').generate(text)
plt.figure(figsize=(14,6))
plt.imshow(wordcloud,interpolation='bilinear')
plt.show()