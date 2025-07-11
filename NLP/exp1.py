import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
text="""Machine Learning,DeepLearning and Natural Language Processing are following the better algorithm playing a key role  in AI concepts"""
words=word_tokenize(text)
print(words)
stop_words=set(stopwords.words('english'))
#remove common english words and store in another list
filtered=[w for w in words if w.lower() not in stop_words]
print(filtered)
#remove special symbols
#import string
remove_pun=[w for w in filtered if w not in string.punctuation]
print(remove_pun)
lemmatizer=WordNetLemmatizer()
