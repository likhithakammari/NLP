import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews,stopward
from nltk.tokenize import word_tokenize
import random
document=[(list(movie_reviews.words(field)),categaries)for category in movie_reviews.categories()for field in movie_reviews.categorie()]
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features=list(all_words)[:2000]
print(word_features)
text=''.join(word_features)*1
wordcloud=WordCloud(width=800,height=400,background_color='white').generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.show()
