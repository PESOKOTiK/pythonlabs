import string

import nltk
from nltk import word_tokenize, WordNetLemmatizer, PorterStemmer
from nltk.corpus import gutenberg
import matplotlib.pyplot as plt
from collections import Counter

#zadanka 1
nltk.download('wordnet')
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

text = gutenberg.raw('chesterton-brown.txt')

word_count = len(nltk.word_tokenize(text))
print(f"Кількість слів у тексті: {word_count}")

tokens = nltk.word_tokenize(text)
word_freq = Counter(tokens)
top_words = word_freq.most_common(10)
print("10 найбільш вживаних слів у тексті:")
for word, freq in top_words:
    print(f"{word}: {freq}")

plt.bar(*zip(*top_words))
plt.title('10 найбільш вживаних слів у тексті')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

stopwords = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stopwords]

filtered_word_freq = Counter(filtered_tokens)
filtered_top_words = filtered_word_freq.most_common(10)
print("10 найбільш вживаних слів після видалення стоп-слів та пунктуації:")
for word, freq in filtered_top_words:
    print(f"{word}: {freq}")

plt.bar(*zip(*filtered_top_words))
plt.title('10 найбільш вживаних слів після видалення стоп-слів та пунктуації')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.show()

#zadanka 2
text_to_save = "In the quaint village of Willowbrook, where cobblestone streets meander beneath ancient oaks, there lived a curious librarian named Amelia. Her days were filled with the rustle of pages and the scent of well-worn books. One peculiar tome, bound in faded leather, whispered secrets of a forgotten realm. Intrigued, Amelia embarked on a journey through mystical lands, encountering enchanted creatures and unraveling the tapestry of time. Moonlit nights saw her poring over star maps, seeking constellations lost to legend. As seasons turned, the library transformed into a haven of wisdom, where the magic of stories transcended the ordinary, and every book held the key to a hidden adventure."
with open("input_text.txt", "w", encoding="utf-8") as file:
    file.write(text_to_save)

# Зчитування тексту з файлу
with open("input_text.txt", "r", encoding="utf-8") as file:
    input_text = file.read()

# Токенізація по словам
tokens = word_tokenize(input_text)

# Лемматизація та стеммінг
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
stemmed_tokens = [stemmer.stem(token) for token in tokens]

# Видалення стоп-слів
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_tokens = [token for token in lemmatized_tokens if token.lower() not in stop_words]

# Видалення пунктуації
filtered_tokens = [token for token in filtered_tokens if token not in string.punctuation]

# Запис обробленого тексту у інший файл
processed_text = " ".join(filtered_tokens)
with open("processed_text.txt", "w", encoding="utf-8") as file:
    file.write(processed_text)

