import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
texts=["I love this movie, its fantastic!","It's okay, not too bad","I hated the movie. Very disappointment"]
sia=SentimentIntensityAnalyzer()
for text in texts:
    scores=sia.polarity_scores(text)
    compound=scores['compound']
    sentiment=("positive" if compound>0.05 else "negative" if compound<0.05 else "neutral")
    print(text)
    print(scores)
    print(sentiment)