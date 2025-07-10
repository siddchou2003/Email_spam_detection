import re
import math
import sys
import csv
import pandas as pd

df = pd.read_csv("spam_ham_dataset.csv")
data = [(row['text'], row['label']) for _, row in df.iterrows() if isinstance(row['text'], str)]

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

spam_words = []
ham_words = []
spam_count = 0
ham_count = 0

for text, label in data:
    words = preprocess(text)
    if label == "spam":
        spam_words.append(words)
        spam_count += 1
    else:
        ham_words.append(words)
        ham_count += 1

vocabulary = set(word for message in spam_words + ham_words for word in message)

def word_frequency(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

spam_word_frequency = word_frequency([word for message in spam_words for word in message])
ham_word_frequency = word_frequency([word for message in ham_words for word in message])

total_length = len(spam_words) + len(ham_words)
p_spam = spam_count / total_length
p_ham = ham_count / total_length

def predict(text):
    words = preprocess(text)

    log_spam_word = math.log(p_spam)
    log_ham_word = math.log(p_ham)

    spam_total_words = sum(spam_word_frequency.values())
    ham_total_words = sum(ham_word_frequency.values())
    vocab_size = len(vocabulary)

    for word in words:
        spam_word_probability = (spam_word_frequency.get(word, 0) + 1) / (spam_total_words + vocab_size)
        ham_word_probability = (ham_word_frequency.get(word, 0) + 1) / (ham_total_words + vocab_size)

        log_spam_word += math.log(spam_word_probability)
        log_ham_word += math.log(ham_word_probability)

    return "spam" if log_spam_word > log_ham_word else "ham"

if __name__ == "__main__":
    message = sys.argv[1]
    print(predict(message))