

import nltk
from nltk.corpus import brown, reuters, stopwords
# from nltk.tokenize import word_tokenize
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

################
####part A - 1

# Download NLTK corpora and stopwords if not already downloaded
nltk.download('brown')
nltk.download('reuters')
nltk.download('stopwords')

# Get stopwords
stop_words = set(stopwords.words('english'))

# Function to calculate word frequency distribution after removing stopwords
def word_frequency_distribution(corpus):
    # words = [word.lower() for word in corpus.words() if word.isalpha() and word.lower() not in stop_words]
    words = [word.lower() for word in corpus.words() if word.lower() not in stop_words]
    word_freq = Counter(words)
    return word_freq

# Get word frequency distribution for Brown and Reuters corpora
brown_freq = word_frequency_distribution(brown)
reuters_freq = word_frequency_distribution(reuters)


################
####part A - 2



# Display top ten words for Brown corpus
print("Top ten words in Brown corpus:")
print("============================================")
for word, freq in brown_freq.most_common(10):
    print(f"{word}: {freq}")

# Display top ten words for Reuters corpus
print("\nTop ten words in Reuters corpus:")
print("============================================")
for word, freq in reuters_freq.most_common(10):
    print(f"{word}: {freq}")

# Create DataFrame for displaying results in table format
data = {
    "Brown Corpus": [word for word, _ in brown_freq.most_common(10)],
    "Brown Frequency": [freq for _, freq in brown_freq.most_common(10)],
    "Reuters Corpus": [word for word, _ in reuters_freq.most_common(10)],
    "Reuters Frequency": [freq for _, freq in reuters_freq.most_common(10)]
}

df = pd.DataFrame(data)
print("\nTop 10 words in both corpora:")
print("============================================")
print(df)



data = {
    "Brown Corpus": [word for word, _ in brown_freq.most_common(20)],
    "Brown Frequency": [freq for _, freq in brown_freq.most_common(20)],
    "Reuters Corpus": [word for word, _ in reuters_freq.most_common(20)],
    "Reuters Frequency": [freq for _, freq in reuters_freq.most_common(20)]
}

df = pd.DataFrame(data)
print("\nTop 20 words in both corpora:")
print("============================================")
print(df)



################
####part A - 3



# Get ranks and frequencies for the first 1000 words
brown_ranks = np.arange(1, 1001)
brown_freq_values = [freq for _, freq in brown_freq.most_common(1000)]
reuters_ranks = np.arange(1, 1001)
reuters_freq_values = [freq for _, freq in reuters_freq.most_common(1000)]

# Take logarithms of ranks and frequencies
log_brown_ranks = np.log(brown_ranks)
log_brown_freq_values = np.log(brown_freq_values)
log_reuters_ranks = np.log(reuters_ranks)
log_reuters_freq_values = np.log(reuters_freq_values)

# Plot log(rank) vs log(frequency) for Brown corpus
plt.figure(figsize=(10, 5))
plt.plot(log_brown_ranks, log_brown_freq_values, marker='o', linestyle='-', color='b')
plt.title("Brown Corpus: log(rank) vs log(frequency)")
plt.xlabel("log(rank)")
plt.ylabel("log(frequency)")
plt.grid(True)
plt.show()

# Plot log(rank) vs log(frequency) for Reuters corpus
plt.figure(figsize=(10, 5))
plt.plot(log_reuters_ranks, log_reuters_freq_values, marker='o', linestyle='-', color='r')
plt.title("Reuters Corpus: log(rank) vs log(frequency)")
plt.xlabel("log(rank)")
plt.ylabel("log(frequency)")
plt.grid(True)
plt.show()















################
####part A - 4


# Reuters corpus
reuters_words = reuters.words()


reuters_word_counts = len(reuters_words)

# Count the occurrences of the word "adiabatic"
count_reuters_additives = reuters_words.count('additives')
count_reuters_home = reuters_words.count('home')

print("reuters_word_counts:", reuters_word_counts)
print("Count of 'additives' in the Reuters corpus:", count_reuters_additives)
print("Count of 'home' in the Reuters corpus:", count_reuters_home)



# brown corpus
brown_words = brown.words()


brown_word_counts = len(brown_words)


# Count the occurrences of the word "additives"
count_brown_additives = brown_words.count('additives')
count_brown_home = brown_words.count('home')


print("brown_word_counts:", brown_word_counts)
print("Count of 'additives' in the Brown corpus:", count_brown_additives)
print("Count of 'home' in the Brown corpus:", count_brown_home)





# reuters_word_counts: 1720901
# Count of 'additives' in the Reuters corpus: 2
# Count of 'home' in the Reuters corpus: 115
# brown_word_counts: 1161192
# Count of 'additives' in the Brown corpus: 4
# Count of 'home' in the Brown corpus: 526

